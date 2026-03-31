from langchain.agents import create_agent, AgentState
from src.prompt_provider.system_prompt import Prompt
from langgraph.checkpoint.memory import InMemorySaver  
import os
from dotenv import load_dotenv
load_dotenv()

debug_mode = os.getenv('AGENT_DEBUG_MODE', 'True')

class CustomAgentState(AgentState):
    user_id: str
    preferences: dict

def get_agent_client(llm, tools: list[str]):
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
        raise Exception(f"Error initializing agent client", str(e))