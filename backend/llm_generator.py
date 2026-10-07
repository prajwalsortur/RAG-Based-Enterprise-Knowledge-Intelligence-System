"""
LLM Generation Module

This file connects the RAG system to the Groq LLM.

Why this file exists:
- It receives the user's question.
- It receives relevant knowledge retrieved from ChromaDB.
- It sends both to the LLM.
- It returns the generated answer.

Connection:
ChromaDB retrieval -> retrieved context -> this file -> Groq LLM -> answer
"""

import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from the .env file.
load_dotenv()

# Read the Groq API key without exposing it in the source code.
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file.")


# Create the Groq client used to communicate with the LLM.
client = Groq(api_key=api_key)


def generate_answer(question, context):
    """
    Generate an answer using the user's question and retrieved knowledge.

    Args:
        question: The user's question.
        context: Relevant information retrieved from ChromaDB.

    Returns:
        The LLM-generated answer.
    """

    prompt = f"""
You are an enterprise knowledge assistant.

Answer the user's question using ONLY the provided knowledge.

If the answer cannot be found in the provided knowledge,
say that the information is not available in the knowledge base.

Do not invent or assume information.

Knowledge:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content