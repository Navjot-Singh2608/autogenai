from fastapi import APIRouter, UploadFile, File
import numpy as np
from ..services.pdf_reader import extract_text_from_pdf, chunk_text, embed_texts
from ..services.web_scraper import extract_text_from_url
from ..utils.memory import uploaded_chunks,uploaded_embeddings
from ..services.searcher import search_chunks
from pydantic import BaseModel
import logging

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    print("Uploading PDF and processing...")
    print("Uploading PDF and processing...", flush=True)

    logging.info("upload file..........")

    content = await file.read()

    # 1. Extract text
    text = extract_text_from_pdf(content)

    # 2. Chunk the text
    chunks = chunk_text(text)

    # 3. Embed the chunks
    embeddings = embed_texts(chunks)

    # 4. Save into global memory
    uploaded_chunks.clear()
    uploaded_chunks.extend(chunks)

    uploaded_embeddings.clear()
    uploaded_embeddings.extend([embedding.tolist() for embedding in embeddings])

    return {
        "message": "PDF uploaded and processed.",
        "num_chunks": len(chunks)
    }


@router.get("/search")
async def search_pdf(query: str):
    print("here are you hhhhhhhhhhhhhhhhhh")
    # Check if there are any chunks or embeddings
    if not uploaded_chunks or not uploaded_embeddings:
        return {"error": "No PDF uploaded or processed yet."}

    # Use the search function from searcher.py, passing the query
    search_result = search_chunks(query, uploaded_chunks, uploaded_embeddings)

    if "error" in search_result:
        return search_result  # Return the error if no data found

    return {
        "result": search_result["best_chunk"],
        "similarity_score": search_result["score"]
    }


@router.post("/fetch-url")
async def fetch_url(url: str):
    print("Fetching URL and processing...")

    # 1. Extract text from URL
    text = extract_text_from_url(url)

    # 2. Chunk the text
    chunks = chunk_text(text)

    # 3. Embed the chunks
    embeddings = embed_texts(chunks)

    return {
        "chunks": chunks,
        "embeddings": [embedding.tolist() for embedding in embeddings]
    }
