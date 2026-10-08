
"""
RAG Pipeline Module

Why this file exists:
- Connects question embedding, ChromaDB retrieval, and LLM generation.
- Provides one function to ask questions against the knowledge base.

Connection:
User question -> embedding_model.py -> vector_store.py
-> llm_generator.py -> final answer
"""

from backend.embedding_model import create_embeddings
from backend.vector_store import search_embeddings
from backend.llm_generator import generate_answer


def ask_question(question: str) -> str:
    """Retrieve relevant knowledge and generate an answer."""

    # Convert the user's question into a numerical vector.
    query_embedding = create_embeddings([question])[0]

    # Search ChromaDB for the three most relevant text chunks.
    results = search_embeddings(query_embedding)
    documents = results.get("documents", [[]])[0]

    if not documents:
        return "The information is not available in the knowledge base."

    # Combine retrieved chunks into context for the LLM.
    context = "\n\n".join(documents)

    # Generate the final answer using the question and retrieved context.
    return generate_answer(question, context)