## Create embeddings and store in vector store
from src.embedding.ollama_embedding import get_embedding_client
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.vectorstores import FAISS
import faiss


def create_vector_store(embedding_model_name: str, documents: list[str]):
    embedding = get_embedding_client(embedding_model_name)
    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embedding
    )

    vector_store.save_local("faiss_index")