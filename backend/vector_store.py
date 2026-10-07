"""
Vector Store Module

Why this file was created:
This file handles the vector database stage of our RAG system.

What it is used for:
It stores text chunks and their embedding vectors in ChromaDB.
This allows us to later search for the most relevant information
when a user asks a question.

How it connects:
text_splitter.py creates text chunks.
embedding_model.py converts those chunks into embedding vectors.
This file stores both the chunks and vectors in ChromaDB.

ChromaDB is used locally so our project does not need a cloud
vector database or an external database server.
"""

import chromadb


# PersistentClient stores the ChromaDB data on our computer.
# This means the stored vectors remain available after the
# Python program is stopped.
client = chromadb.PersistentClient(path="chroma_db")


# A collection is similar to a table in a traditional database.
# Our collection will contain the enterprise knowledge chunks
# and their corresponding embedding vectors.
collection = client.get_or_create_collection(
    name="enterprise_knowledge"
)


def store_embeddings(
    chunks: list[str],
    embeddings: list[list[float]]
) -> None:
    """
    Store text chunks and their embedding vectors in ChromaDB.

    Args:
        chunks: Text chunks created by text_splitter.py.
        embeddings: Vectors created by embedding_model.py.
    """

    # Create a unique ID for every chunk.
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Store the chunks and their vectors together.
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )

def search_embeddings(
    query_embedding: list[float],
    n_results: int = 3
):
    """
    Search ChromaDB for the most relevant knowledge chunks.

    Args:
        query_embedding: Vector representation of the user's question.
        n_results: Number of relevant chunks to retrieve.

    Returns:
        Matching documents, IDs, and similarity distances.
    """

    # ChromaDB compares the question vector with stored vectors
    # and returns the most relevant knowledge chunks.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )

    return results