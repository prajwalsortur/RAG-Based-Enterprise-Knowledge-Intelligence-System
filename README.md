# RAG-Based Enterprise Knowledge Intelligence System

An AI-powered knowledge assistant that uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from enterprise documents and generate context-grounded answers.

The goal of this project is to make organizational knowledge easier to access while reducing unsupported AI responses.

## Project Overview

Enterprise organizations maintain important information in documents such as HR policies, employee guidelines, technical documentation, and internal knowledge bases. Finding specific information manually can be time-consuming.

This project combines document processing, semantic search, vector storage, and Large Language Model (LLM) generation to build a knowledge intelligence system.

## Objectives

* Extract text from enterprise PDF documents.
* Split extracted text into smaller, meaningful chunks.
* Convert text chunks into numerical embeddings.
* Store embeddings in a vector database.
* Retrieve relevant information based on user queries.
* Generate answers using retrieved context and an LLM.
* Provide a frontend for interacting with the knowledge system.
* Build the system incrementally with an emphasis on maintainability and answer reliability.

## Technology Stack

| Technology      | Purpose                                    |
| --------------- | ------------------------------------------ |
| Python          | Core RAG pipeline and backend logic        |
| PyMuPDF         | Extracting text from PDF documents         |
| Embedding model | Converting text into numerical vectors     |
| ChromaDB        | Storing and retrieving document embeddings |
| Groq API        | LLM-powered answer generation              |
| FastAPI         | Backend API development                    |
| React           | Frontend user interface                    |
| Vite            | Frontend development and build tooling     |
| Git and GitHub  | Version control and project tracking       |

## RAG Architecture

The system follows this workflow:

1. **Document ingestion:** Load a PDF containing enterprise knowledge.
2. **Text extraction:** Extract readable text using PyMuPDF.
3. **Text chunking:** Divide the extracted text into smaller chunks.
4. **Embedding generation:** Convert chunks into numerical vectors.
5. **Vector storage:** Store chunks and their embeddings in ChromaDB.
6. **Retrieval:** Search for relevant chunks based on the user's question.
7. **LLM generation:** Send the retrieved context and question to the Groq-powered language model.
8. **Response delivery:** Return the generated answer through the application interface.

## Work Completed So Far

### 1. Project Setup

* Created the GitHub repository and local project structure.
* Organized the project into `backend`, `data`, and `frontend` directories.
* Created a Python virtual environment.
* Configured Git and `.gitignore` to exclude virtual environments, Python cache files, and environment secrets.

### 2. PDF Document Loader

* Created `backend/document_loader.py`.
* Used PyMuPDF to extract text from PDF documents.
* Added a sample enterprise knowledge document at `data/enterprise_knowledge.pdf`.
* Tested the document loader and verified that the expected text could be extracted.

The sample document contains fictional TechNova Solutions HR information, including working hours, paid leave, remote-work guidelines, and IT support details.

### 3. Text Chunking

* Created `backend/text_splitter.py`.
* Implemented the text-splitting stage to divide extracted document content into smaller chunks.
* Connected the chunking stage to the document-loading workflow.

### 4. Embedding Generation

* Created `backend/embedding_model.py`.
* Implemented the embedding-generation stage.
* Connected document chunks to the embedding process.

### 5. Vector Database and Retrieval

* Created `backend/vector_store.py`.
* Integrated ChromaDB for vector storage.
* Implemented storage and retrieval functionality.
* Tested the pipeline to confirm that document chunks and embeddings could be stored in the collection.

### 6. LLM Answer Generation

* Implemented the LLM generation stage using the Groq API.
* Connected the language model to the retrieval workflow.
* Prepared the pipeline to generate answers using retrieved document context.

### 7. Frontend Setup

* Created the `frontend` application structure.
* Initialized the React and Vite frontend project.
* Started organizing the frontend files for the knowledge assistant interface.

## Current Project Structure

```text
RAG-KNOWLEDGE-SYSTEM/
│
├── backend/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embedding_model.py
│   ├── vector_store.py
│   └── main.py
│
├── data/
│   └── enterprise_knowledge.pdf
│
├── frontend/
│   ├── src/
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   ├── index.html
│   └── ...
│
├── .gitignore
└── README.md
```

*Note: This structure reflects the files established during development. Additional frontend files and configuration files may exist in the repository.*

## Sample Use Case

A user wants to know the organization's remote-work policy.

**User question:**

"What is the remote-work policy?"

**System workflow:**

* The system processes the question.
* ChromaDB retrieves relevant document chunks.
* The retrieved context is provided to the language model.
* The model generates an answer based on the available context.

**Expected answer based on the sample document:**

"Employees can work remotely up to two days per week, subject to manager approval."

## Installation and Setup

### Prerequisites

* Python installed on your system.
* Node.js and npm installed.
* Git installed.
* A Groq API key for LLM generation.

### Backend Setup

Open PowerShell in the project root:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the Python dependencies required by the project. Keep your API key in a local `.env` file or environment variable, according to the backend configuration. Never commit API keys to GitHub.

### Frontend Setup

```powershell
cd frontend
npm install
npm run dev
```

Use the local URL displayed by Vite to open the frontend.

*The exact backend launch command and dependency installation instructions should match the final `main.py` and dependency configuration.*

## Reliability and Hallucination Reduction

An important objective is to reduce unsupported responses by grounding answer generation in retrieved document content.

Planned improvements include:

* Improve retrieval relevance.
* Handle questions whose answers are missing from the documents.
* Provide source references for generated answers.
* Test answers against known questions and expected results.
* Improve error handling for document processing, retrieval, and API failures.

Retrieval-augmented generation can reduce hallucinations, but it does not guarantee that every generated answer is correct.

## Development Roadmap

* [x] Project foundation and GitHub setup
* [x] PDF text extraction
* [x] Text chunking
* [x] Embedding generation
* [x] ChromaDB vector storage and retrieval
* [x] Groq-based LLM generation stage
* [x] React and Vite frontend initialization
* [ ] Complete and connect the frontend interface to the backend
* [ ] Test the complete end-to-end question-answering workflow
* [ ] Improve responses when relevant information is unavailable
* [ ] Add source citations to answers
* [ ] Support multiple documents and document updates
* [ ] Add automated tests and retrieval-quality evaluation
* [ ] Prepare the application for deployment


## Project Status

**Status: Under active development.**

The core RAG processing components have been implemented incrementally, and the frontend setup has begun. Completing and validating the integrated application is the next major objective.

## Author

**Prajwal Sortur**

GitHub: https://github.com/prajwalsortur

Repository: https://github.com/prajwalsortur/RAG-Based-Enterprise-Knowledge-Intelligence-System
