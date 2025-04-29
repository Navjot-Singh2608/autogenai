import numpy as np
import re
from typing import List, Optional
from ..utils.vocab import vocab as default_vocab
from ..utils.memory import uploaded_embeddings,uploaded_chunks

STOPWORDS = set([
    'the', 'is', 'and', 'to', 'a', 'of', 'in', 'that', 'it', 'for', 'on', 'with', 'as', 'at', 'this', 'by', 'an'
])

def clean_text(text: str) -> str:
    """
    Lowercase the text, remove special characters, and extra spaces.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Keep only alphanumerics
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

def tokenize(text: str) -> List[str]:
    """
    Split cleaned text into tokens (words).
    """
    return text.split()

def remove_stopwords(words: List[str]) -> List[str]:
    """
    Remove common English stopwords.
    """
    return [word for word in words if word not in STOPWORDS]

def simple_text_embedding(
    text: str,
    vocab: Optional[List[str]] = None
) -> np.ndarray:
    """
    Create a simple embedding vector based on word frequencies.
    """
    if vocab is None:
        vocab = default_vocab

    text = clean_text(text)
    words = tokenize(text)
    words = remove_stopwords(words)

    vector = np.zeros(len(vocab))

    for i, vocab_word in enumerate(vocab):
        vector[i] = words.count(vocab_word)

    return vector

def chunk_text(text, chunk_size=500):
    """
    Chunk the text into smaller parts (with a given chunk size).
    """
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    uploaded_chunks.clear()  # Clear previous chunks
    uploaded_chunks.extend(chunks)  # Store new chunks in memory
    return chunks

def embed_texts(chunks):
    """
    Embed the chunks into vectors (simple text embedding).
    """
    embeddings = [simple_text_embedding(chunk) for chunk in chunks]
    uploaded_embeddings.clear()  # Clear previous embeddings
    uploaded_embeddings.extend(embeddings)  # Store new embeddings in memory
    return embeddings