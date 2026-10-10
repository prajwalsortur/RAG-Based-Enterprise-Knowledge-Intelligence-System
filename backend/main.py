"""
FastAPI Backend Entry Point

Why this file exists:
- Provides an API for the RAG system.
- Receives questions from a frontend or API client.
- Sends questions to the RAG pipeline.
- Returns the generated answer.

Connection:
Client -> FastAPI -> rag_pipeline.py -> RAG components -> Answer
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.rag_pipeline import ask_question


# Create the FastAPI application.
app = FastAPI(title="Enterprise Knowledge Intelligence System")

# Allow the local React frontend to communicate with this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class QuestionRequest(BaseModel):
    """Request format expected by the /ask endpoint."""

    question: str


@app.get("/")
def home():
    """Check whether the API server is running."""
    return {"message": "RAG Knowledge System API is running."}


@app.post("/ask")
def ask(request: QuestionRequest):
    """Receive a question and return a RAG-generated answer."""
    answer = ask_question(request.question)

    return {"answer": answer}