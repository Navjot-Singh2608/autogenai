from PyPDF2 import PdfReader
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(file_content):
    reader = PdfReader(file_content)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def embed_texts(chunks):
    embeddings = []
    for chunk in chunks:
        response = openai.Embedding.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings.append(response["data"][0]["embedding"])
    return embeddings
