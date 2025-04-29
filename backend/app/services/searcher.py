# searcher.py
import numpy as np
from ..services.text_processing import simple_text_embedding


def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Compute the cosine similarity between two vectors.
    """
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def search_chunks(query: str, chunks: list, embeddings: list) -> dict:
    """
    Search the uploaded chunks for the query.
    """

    # 1. Embed the query
    query_embedding = simple_text_embedding(query)

    # 2. Find the most similar chunk
    best_score = -1
    best_chunk = ""

    for chunk, embedding in zip(chunks, embeddings):
        embedding = np.array(embedding)  # Convert list back to numpy array
        score = cosine_similarity(query_embedding, embedding)

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return {
        "best_chunk": best_chunk,
        "score": best_score
    }
