## Document ingestion
import pymupdf4llm
from langchain_core.documents import Document

def extract_text_from_pdf(pdf_file_path):
    md = pymupdf4llm.to_markdown(pdf_file_path)
    return [
        Document(
            page_content=md,
            metadata={"source": pdf_file_path}
        )
    ]
