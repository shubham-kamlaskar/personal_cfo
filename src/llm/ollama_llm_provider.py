import os
from dotenv import load_dotenv
load_dotenv()
from langchain_ollama import ChatOllama
from ollama import Client
class LLMProvider:
    def __init__(self):
        self.llm_model_name = str(os.getenv('LLM_MODEL_NAME'))
        self.llm_temperature = float(os.getenv('LLM_TEMPERATURE'))
        
    def llm_client(self):
        try:
            llm = ChatOllama(
                model=self.llm_model_name,
                validate_model_on_init=True,
                temperature=self.llm_temperature,
            )
            
            return llm
        except Exception as e:
            print(f"Error initializing Ollama llm_client", str(e))
            raise Exception(f"Error initializing Ollama llm_client", str(e))

    def conversation_summary_generator(self):
        """Function is used to generate the summary of conversation."""
        llm = self.llm_client()
        
        