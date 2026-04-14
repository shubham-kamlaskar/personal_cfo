import os
from dotenv import load_dotenv
load_dotenv()
import uuid

import markdown

from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver
from typing import List
from langchain.tools import BaseTool

from src.prompt_provider.prompt_store import Prompt
from src.tool_provider.tool_calls import tools
from src.llm_provider.ollama_llm_provider import LLMProvider
from src.models.user_activity_model import ConversationObject
from src.database_provider.mongo_client import MongoDBClient
from src.util.datetime_helper import get_current_dt_in_milliseconds_precision

debug_mode = os.getenv('AGENT_DEBUG_MODE', 'True')
memory_checkpointer = InMemorySaver()
mongodb_client = MongoDBClient()
llm_provider = LLMProvider()
user_info_collection = str(os.getenv('USER_INFO_COLLECTION'))
db_name = str(os.getenv('DB_NAME')) 

class CustomAgentState(AgentState):
    user_id: str
    preferences: dict
    
class AgentProvider:
    def __init__(self):
        self.ai_agent_name = str(os.getenv('AI_AGENT_NAME'))
        self.ai_agent_version = str(os.getenv("AI_AGENT_VERSION"))
        self.db_name = str(os.getenv('DB_NAME'))
        self.conversation_collection = str(os.getenv("CONVERSATION_COLLETION"))
        self.agent = None
        self.session_id = "81d9c347-f032-455e-9805-77e6e9198abc"

    async def get_agent_client(self, tools: List[BaseTool], user_id: str):
        try:
            user_info = mongodb_client.find_one_item_from_collection(db_name, user_info_collection, "user_id", user_id)
            
            if self.agent is None:    
                self.agent = create_agent(
                    model=llm_provider.llm_client(),
                    tools=tools,
                    system_prompt=(Prompt.DEFAULT_SYSTEM_PROMPT + Prompt.TASK_PROMPT + Prompt.CURRENT_DATE_CONTEXT_PROMPT +
                                Prompt.THINKING_AND_REASONING_PROMPT + Prompt.GENERAL_GUIDELINES_PROMPT +Prompt.INFORMATION_NOT_ALLOWED_PROMPT
                                 + f"Use attached information to give personalized responses {str(user_info)}"),
                    state_schema=CustomAgentState,
                    checkpointer=memory_checkpointer,
                    debug=bool(debug_mode),
                )

        except Exception as e:
            print(f"Error initializing agent client: {str(e)}")
            raise Exception(f"Error initializing agent client: {str(e)}")
        
    async def get_agent_response(self, user_query: str, user_id: str):
        try:
            answer = None
            if self.agent is None:
                await self.get_agent_client(tools, user_id)
                
            response = self.agent.invoke(
                {
                    "messages": [{"role": "user", "content": user_query}],
                    "user_id": user_id,
                    "preferences": {"theme": "dark"}
                },
                {"configurable": {"thread_id": self.session_id}}
            )
            if response:
                messages = response.get("messages", [])

                response_call = messages[-1] if messages else None
                tool_call: dict = messages[-2] if len(messages) >= 2 else None

                usage: dict = getattr(response_call, "usage_metadata", None)
                metadata: dict = getattr(response_call, "response_metadata", None)

                response_object = ConversationObject(
                    user_id = user_id,
                    query=user_query,
                    response=response_call.content if response_call else "",
                    session_id = self.session_id,
                    conversation_id = None,
                    message_id = getattr(tool_call, "id", None),
                    agent = {
                        "agent_name": self.ai_agent_name,
                        "agent_version": self.ai_agent_version,
                        "model": metadata.get('model', None),
                        "tool_name": getattr(tool_call, "name", None),
                        "tool_status": True,
                        "tool_call_id": getattr(tool_call, "tool_call_id", None),
                    },
                    token_count = {
                        "input_tokens": usage.get('input_tokens', 0),
                        "output_tokens": usage.get('output_tokens', 0),
                        "total_tokens": usage.get('total_tokens', 0),
                    },
                    latency_ms = None,
                    error = None,
                    status = None,
                    createdAt = metadata.get('created_at', None),
                    updatedAt= metadata.get('created_at', None),
                )

                mongodb_client.insert_one_item_in_collection(database_name=self.db_name,
                                                             collection_name=self.conversation_collection,
                                                             data=response_object.model_dump())
                answer = response_call.content
            else:
                answer =  "Failed to generate any response."
                
            return answer   

        except Exception as e:
            print(f"Error getting agent response: {str(e)}")
            raise Exception(f"Error getting agent response: {str(e)}")
        
    
    def _generate_new_thread_id(self):
        """Functions is used to generate new thread id when clicked on new chat button"""
        new_thread_id = "session" + str(uuid.uuid4())
        self.thread_id = new_thread_id
        