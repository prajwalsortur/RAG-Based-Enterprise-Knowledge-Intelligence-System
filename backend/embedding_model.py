"""
Embedding Model Module

Why this file was created:
This file handles the embedding stage of our RAG system.

What it is used for:
It converts text chunks into numerical vectors that represent
the meaning of the text.

How it connects:
text_splitter.py creates text chunks.
This file converts those chunks into embedding vectors.
The vectors will later be stored in a vector database
for semantic search and retrieval.
"""

from sentence_transformers import SentenceTransformer


# Free, local embedding model used to convert text into vectors.
MODEL_NAME = "all-MiniLM-L6-v2"


# Load the embedding model once so it can be reused.
model = SentenceTransformer(MODEL_NAME)


def create_embeddings(chunks: list[str]) -> list[list[float]]:
    """
    Convert text chunks into numerical embedding vectors.

    Args:
        chunks: A list of text chunks.

    Returns:
        A list of embedding vectors.
    """

    embeddings = model.encode(chunks)

    return embeddings.tolist()