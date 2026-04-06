from langchain_ollama import OllamaEmbeddings

def get_embedding_client(model_name: str):
    try:
        embeddings = OllamaEmbeddings(
            model=model_name,
            validate_model_on_init=True)
        
        return embeddings
    except Exception as e:
        raise Exception(f"An error occcured during get_embedding_client method: {str(e)}")