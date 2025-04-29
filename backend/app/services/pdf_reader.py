import fitz  # PyMuPDF
from io import BytesIO
import numpy as np
from typing import List, Optional
from .text_processing import simple_text_embedding

def extract_text_from_pdf(file_bytes: bytes) -> str:
    doc = fitz.open(stream=BytesIO(file_bytes), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
    """
    Splits text into smaller chunks of specified size.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def embed_texts(chunks: List[str]) -> List[np.ndarray]:
    """
    Embed each chunk using simple_text_embedding.
    """
    embeddings = []
    for chunk in chunks:
        embedding = simple_text_embedding(chunk)
        embeddings.append(embedding)
    return embeddings


