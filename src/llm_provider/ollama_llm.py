from langchain_ollama import ChatOllama

def llm_client(llm_model_name: str, llm_temperature: float):
    try:
        llm = ChatOllama(
            model=llm_model_name,
            validate_model_on_init=True,
            temperature=llm_temperature,
        )
        
        return llm
    except Exception as e:
        raise Exception(f"Error initializing Ollama llm_client", str(e))