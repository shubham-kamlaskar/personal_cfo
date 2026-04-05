import os
from dotenv import load_dotenv
load_dotenv()

import markdown

from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver
from typing import List
from langchain.tools import BaseTool

from src.prompt_provider.prompt_store import Prompt
from src.tool_provider.tool_calls import tools
from src.llm_provider.ollama_llm import llm_client
from src.models.response_object import ResponseObject

debug_mode = os.getenv('AGENT_DEBUG_MODE', 'True')
memory_checkpointer = InMemorySaver()

class CustomAgentState(AgentState):
    user_id: str
    preferences: dict
    
class AgentProvider:
    def __init__(self):
        self.llm_model_name=os.getenv('LLM_MODEL_NAME')
        self.llm_temperature=os.getenv('LLM_TEMPERATURE')
        

    async def get_agent_client(self, llm, tools: List[BaseTool]):
        try:
            agent = create_agent(
                model=llm,
                tools=tools,
                system_prompt=(Prompt.DEFAULT_SYSTEM_PROMPT + Prompt.TASK_PROMPT + Prompt.INFOMRATION_NOT_ALLOWED_PROMPT),
                state_schema=CustomAgentState,
                checkpointer=memory_checkpointer,
                debug=bool(debug_mode),
            )
            
            return agent
        except Exception as e:
            raise Exception(f"Error initializing agent client: {str(e)}")
        
    async def get_agent_response(self, user_query: str):
        try:
            llm = llm_client(
                llm_model_name=self.llm_model_name,
                llm_temperature=self.llm_temperature
            )

            agent = await self.get_agent_client(llm, tools)

            response = await agent.ainvoke(
                {
                    "messages": [{"role": "user", "content": user_query}],
                    "user_id": "user_123",
                    "preferences": {"theme": "dark"}
                },
                {"configurable": {"thread_id": "1"}}
            )

            messages = response.get("messages", [])

            response_call = messages[-1] if messages else None
            tool_call = messages[-2] if len(messages) >= 2 else None

            usage = getattr(response_call, "usage_metadata", None)
            metadata = getattr(response_call, "response_metadata", None)

            response_object = ResponseObject(
                query=user_query,
                tool_name=getattr(tool_call, "name", None),
                tool_status=True,
                tool_call_id=getattr(tool_call, "tool_call_id", None),
                input_tokens=usage.get('input_tokens', 0),
                output_tokens=usage.get('output_tokens', 0),
                total_tokens=usage.get('total_tokens', 0),
                model=metadata.get('model', None),
                created_at=metadata.get('created_at', None),
                response=response_call.content if response_call else ""
            )

            return markdown.markdown(response_call.content)

        except Exception as e:
            raise RuntimeError("Error getting agent response") from e