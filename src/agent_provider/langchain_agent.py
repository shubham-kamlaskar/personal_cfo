from langchain.agents import create_agent
from src.prompt_provider.system_prompt import Prompt

def get_agent_client(llm, tools: list[str]):
    try:
        agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt=(Prompt.DEFAULT_SYSTEM_PROMPT + Prompt.TASK_PROMPT + Prompt.INFOMRATION_NOT_ALLOWED_PROMPT)
        )
        
        return agent
    except Exception as e:
        raise Exception(f"Error initializing agent client", str(e))