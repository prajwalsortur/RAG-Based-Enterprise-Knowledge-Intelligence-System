# RAG-Based Enterprise Knowledge Intelligence System

An AI-powered enterprise knowledge assistant that answers questions using information retrieved from company documents. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant document content and generate context-based answers.

## Overview

Employees often need to search through company documents to find information about workplace policies, working hours, leave policies, and other internal information.

This project provides a conversational interface where users can ask questions in natural language and receive answers based on the available knowledge base.

## Features

- **PDF Document Loading:** Extracts text from enterprise PDF documents.
- **Text Chunking:** Splits extracted text into smaller chunks for efficient retrieval.
- **Text Embeddings:** Converts text chunks into numerical representations for semantic search.
- **Vector Database:** Uses ChromaDB to store and retrieve document embeddings.
- **Semantic Search:** Retrieves relevant document chunks based on user questions.
- **LLM-Based Answer Generation:** Uses the Groq API to generate answers from retrieved context.
- **FastAPI Backend:** Provides an API endpoint for processing questions.
- **React Frontend:** Provides an interactive chat interface.
- **Markdown Rendering:** Displays formatted AI responses.
- **Enter-to-Send:** Allows users to submit questions using the Enter key.
- **Clear Chat:** Allows users to clear the current conversation.
- **Automatic Chat Scrolling:** Keeps the latest messages visible as the conversation grows.
- **Error Handling:** Displays an error message when the backend cannot process a request.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | React, Vite, JavaScript |
| Backend | FastAPI |
| PDF Processing | PyMuPDF |
| Text Chunking | LangChain Text Splitters |
| Embedding Model | Sentence Transformers |
| Vector Database | ChromaDB |
| Large Language Model API | Groq |
| API Communication | REST API |
| Version Control | Git and GitHub |

## System Architecture

```text
Enterprise PDF Documents
          |
          v
    PDF Text Loader
          |
          v
      Text Chunking
          |
          v
   Embedding Model
          |
          v
   ChromaDB Vector Store
          |
          v
     User Question
          |
          v
   Question Embedding
          |
          v
  Relevant Chunk Retrieval
          |
          v
     Groq LLM
          |
          v
     Generated Answer
          |
          v
      FastAPI Backend
          |
          v
       React Chat UI
```

## How It Works

1. **Document Loading:** The system extracts text from the enterprise knowledge PDF.
2. **Text Chunking:** The extracted text is divided into smaller, manageable chunks.
3. **Embedding Generation:** The embedding model converts the chunks into numerical vectors.
4. **Vector Storage:** ChromaDB stores the vectors and their associated text.
5. **Question Processing:** The user submits a question through the React chat interface.
6. **Relevant Information Retrieval:** The system searches the vector database for relevant chunks.
7. **Answer Generation:** The retrieved context is passed to the Groq-powered language model to generate an answer.
8. **Answer Display:** FastAPI returns the answer to the frontend, where it is displayed in the chat interface.

## Project Structure

```text
RAG-KNOWLEDGE-SYSTEM/
|
|-- backend/
|   |-- document_loader.py
|   |-- text_splitter.py
|   |-- embedding_model.py
|   |-- vector_store.py
|   |-- llm_generator.py
|   |-- rag_pipeline.py
|   |-- main.py
|
|-- frontend/
|   |-- src/
|   |   |-- App.jsx
|   |   |-- App.css
|   |   |-- index.css
|   |   |-- main.jsx
|   |-- package.json
|   |-- index.html
|
|-- data/
|   |-- enterprise_knowledge.pdf
|
|-- chroma_db/
|-- .gitignore
|-- README.md
```

*Note: Generated database files, environment files, and other local files may vary depending on your setup. The structure above highlights the main project components.*

## Prerequisites

Install the following before running the project:

- Python
- Node.js and npm
- Git
- A Groq API key

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/prajwalsortur/RAG-Based-Enterprise-Knowledge-Intelligence-System.git
cd RAG-Based-Enterprise-Knowledge-Intelligence-System
```

### 2. Set up the Python environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required Python packages:

```bash
pip install fastapi uvicorn pymupdf python-dotenv groq sentence-transformers chromadb langchain-text-splitters
```

### 3. Configure the Groq API key

Create a `.env` file in the project root and add your own API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual key. Never commit your `.env` file or publish your API key.

### 4. Start the backend

From the project root, run:

```bash
uvicorn backend.main:app --reload
```

The FastAPI backend will be available at:

http://127.0.0.1:8000

You can check the API's root endpoint at:

http://127.0.0.1:8000/

### 5. Start the frontend

Open a second terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install the frontend dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open the local URL displayed in your terminal, usually:

http://localhost:5173/

Keep both the backend and frontend running while using the application.

## API Endpoint

### POST `/ask`

Processes a user question and returns an AI-generated answer.

**Request body:**

```json
{
  "question": "How many paid leave days do employees get per year?"
}
```

**Example response:**

```json
{
  "answer": "Employees receive 18 paid leave days per year."
}
```

The actual answer format may vary depending on the retrieved context and language model response.

## Example Questions

Using the sample enterprise knowledge document, try questions such as:

- How many paid leave days do employees get per year?
- How many days per week can employees work remotely?
- What are the company's working hours?
- Which team handles IT support?
- What information is available about company policies?

The system should respond based on the information retrieved from the knowledge base. Questions not supported by the available documents should be handled as unavailable information rather than answered with invented facts.

## Current Project Status

**Completed:**

- PDF text extraction
- Text chunking
- Embedding generation
- ChromaDB vector storage and retrieval
- Groq-powered answer generation
- RAG pipeline integration
- FastAPI backend and question endpoint
- React chat interface
- Frontend-backend integration
- Markdown-formatted answers
- Enter-to-send functionality
- Clear Chat functionality
- Automatic scrolling to the latest chat message
- Chat layout and scrolling improvements

**Future Improvements:**

- Suggested questions
- Improved loading animations
- Displaying retrieved document sources
- Support for uploading additional enterprise documents
- Improved retrieval evaluation and answer quality
- Deployment of the complete application

## Security Notes

- Keep API keys in environment variables.
- Do not commit `.env`, virtual environments, or `node_modules`.
- Do not upload confidential company documents to a public repository.
- Configure CORS appropriately before deploying the application.

## Future Scope

The system can be extended into a more complete enterprise knowledge assistant by supporting multiple documents, document-source citations, improved retrieval evaluation, and deployment for remote access.

## Author

**Prajwal Sortur**

GitHub: https://github.com/p
