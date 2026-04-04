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
                checkpointer=InMemorySaver(),
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

            response = agent.invoke(
                {
                    "messages": [{"role": "user", "content": user_query}],
                    "user_id": "user_123",
                    "preferences": {"theme": "dark"}
                },
                {"configurable": {"thread_id": "1"}}
            )
            tool_call = response["messages"][-2]
            response_call = response['messages'][-1]
            response_object = ResponseObject(
                query=user_query,
                tool_name=tool_call.name,
                tool_status=True,  # Assuming the tool call was successful
                tool_call_id=tool_call.tool_call_id,
                input_tokens=response_call.usage_metadata.input_tokens,
                output_tokens=response_call.usage_metadata.output_tokens,
                total_tokens=response_call.usage_metadata.total_tokens,
                model=response_call.response_metadata.model,
                created_at=response_call.response_metadata.created_at,
                response=response_call.content
            )
            answer = response_call.content
            return markdown.markdown(answer)

        except Exception as e:
            raise Exception(f"Error getting agent response: {str(e)}")
