## Document chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_document_in_chunks(document: str, chunk_size: int, chunk_overlap: int):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(document)
    return texts