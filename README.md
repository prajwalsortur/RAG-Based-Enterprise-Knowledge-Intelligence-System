# RAG-Based Enterprise Knowledge Intelligence System

An AI-powered enterprise knowledge assistant that uses **Retrieval-Augmented Generation (RAG)** to answer questions using information retrieved from company documents. Built with Python, FastAPI, Sentence Transformers, ChromaDB, Groq, and React.

## 🚀 Project Overview

Organizations store important information in HR policies, employee handbooks, technical documentation, and internal knowledge bases. Finding specific information manually can be time-consuming.

This project provides a web-based AI assistant that allows users to ask questions in natural language and receive answers based on relevant information retrieved from an enterprise knowledge base.

The application connects a React frontend to a FastAPI backend, which processes questions through a RAG pipeline and uses a Large Language Model (LLM) to generate answers.

## ✨ Key Features

- **PDF Text Extraction:** Extracts text from enterprise PDF documents using PyMuPDF.
- **Text Chunking:** Splits extracted content into smaller, overlapping text sections.
- **Text Embeddings:** Converts text into numerical vector representations using Sentence Transformers.
- **Vector Database:** Uses ChromaDB to store and retrieve relevant document information.
- **Semantic Search:** Retrieves information based on the meaning of a user's question.
- **LLM Integration:** Uses the Groq API to generate answers from retrieved context.
- **REST API:** Provides a question-answering endpoint through FastAPI.
- **Interactive Web Interface:** Uses React and Vite to provide a simple chat experience.
- **Knowledge-Grounded Answers:** Supplies retrieved document content to the LLM to help reduce unsupported responses.

## 🧠 What Is RAG?

**RAG stands for Retrieval-Augmented Generation.**

Instead of asking an AI model to answer a question using only its general training knowledge, RAG first retrieves relevant information from a selected knowledge source. The retrieved information is then supplied to the language model to help generate a more relevant answer.

### How RAG Works in This Project

```text
Enterprise PDF Document
          |
          v
    Text Extraction
          |
          v
      Text Chunking
          |
          v
   Embedding Generation
          |
          v
       ChromaDB
    Vector Storage
          |
          |
User Question
      |
      v
 FastAPI Backend
      |
      v
 Question Embedding
      |
      v
 Semantic Retrieval
      |
      v
 Relevant Text Chunks
      |
      v
   Groq LLM API
      |
      v
  Generated Answer
      |
      v
 React Chat Interface
```

## 🔄 How It Works

1. **Document Loading:** The system loads the sample enterprise PDF.
2. **Text Extraction:** PyMuPDF extracts readable text from the document.
3. **Text Chunking:** LangChain text splitters divide the content into manageable sections.
4. **Embedding Generation:** Sentence Transformers converts the text chunks into embeddings.
5. **Vector Storage:** ChromaDB stores the document representations for similarity search.
6. **Question Processing:** The user submits a question through the React interface.
7. **Information Retrieval:** The backend retrieves relevant information from the vector database.
8. **Answer Generation:** The retrieved context is passed to the Groq-powered LLM.
9. **Response Display:** The backend returns the answer, and the frontend displays it to the user.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic |
| PyMuPDF | PDF text extraction |
| LangChain Text Splitters | Text chunking |
| Sentence Transformers | Text embedding generation |
| ChromaDB | Vector storage and similarity search |
| Groq API | LLM-powered answer generation |
| FastAPI | REST API backend |
| Uvicorn | ASGI server |
| React | Frontend user interface |
| Vite | Frontend development server |
| CSS | Interface styling |
| Git and GitHub | Version control and project hosting |

## 📁 Project Structure

```text
RAG-Based-Enterprise-Knowledge-Intelligence-System/
│
├── backend/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embedding_model.py
│   ├── rag_pipeline.py
│   ├── llm_generator.py
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── .gitignore
│
├── data/
│   └── enterprise_knowledge.pdf
│
├── chroma_db/
├── .gitignore
└── README.md
```

*Note: Generated files, local environment files, and additional configuration files may be excluded from this overview.*

### Main Backend Components

- `document_loader.py` — Loads the enterprise PDF and extracts its text.
- `text_splitter.py` — Splits extracted text into smaller chunks.
- `embedding_model.py` — Handles embedding generation for semantic search.
- `rag_pipeline.py` — Connects document processing, retrieval, and the RAG workflow.
- `llm_generator.py` — Integrates the Groq API for answer generation.
- `main.py` — Creates the FastAPI application and exposes the question-answering endpoint.

### Main Frontend Components

- `App.jsx` — Implements the main React application interface.
- `App.css` — Contains application-specific styling.
- `index.css` — Contains global styles.
- `main.jsx` — Entry point for rendering the React application.
- `package.json` — Defines frontend dependencies and scripts.

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project:

- Python
- Node.js and npm
- Git
- A Groq API key

### 1. Clone the Repository

Open PowerShell and run:

```powershell
git clone https://github.com/prajwalsortur/RAG-Based-Enterprise-Knowledge-Intelligence-System.git

cd RAG-Based-Enterprise-Knowledge-Intelligence-System
```

### 2. Create a Python Virtual Environment

```powershell
python -m venv venv
```

Activate the environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the backend dependencies:

```powershell
pip install pymupdf langchain-text-splitters sentence-transformers chromadb groq python-dotenv fastapi uvicorn
```

### 3. Configure the Groq API Key

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual API key.

**Security:** Never commit your `.env` file or expose your API key in source code or public repositories.

### 4. Start the Backend

Open PowerShell in the project root and run:

```powershell
cd backend
uvicorn main:app --reload
```

The backend should run at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

Keep this terminal running.

### 5. Start the Frontend

Open a second PowerShell terminal and navigate to the project directory:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite, usually:

http://localhost:5173

Keep both the backend and frontend running while using the application.

*Note: The frontend API configuration must point to the running FastAPI backend. The commands above assume the repository's current local development configuration.*

## 🔌 API Usage

The backend exposes a question-answering endpoint.

**Endpoint:** `POST /ask`

**Local URL:** `http://127.0.0.1:8000/ask`

### Example Request

```json
{
  "question": "How many paid leave days do employees receive per year?"
}
```

### Example Response

```json
{
  "answer": "Employees receive 18 paid leave days per year."
}
```

The example answer is based on the included sample enterprise knowledge document. Actual responses depend on the retrieved context and the language model.

## 💡 Example Questions

Try asking the knowledge assistant:

- How many paid leave days do employees receive per year?
- What are the company's working hours?
- How many days per week can employees work remotely?
- Which team handles IT support?

These questions demonstrate how users can retrieve information from an enterprise knowledge base using natural language.

## 🎯 Project Objectives

- Build an end-to-end Retrieval-Augmented Generation application.
- Understand document processing and semantic search.
- Integrate a vector database with a Large Language Model.
- Develop REST APIs using FastAPI.
- Connect an AI backend to a React frontend.
- Explore practical applications of Generative AI for enterprise knowledge management.

## 🔮 Future Improvements

Potential enhancements include:

- Support for multiple document formats.
- Document upload and management through the interface.
- Source and page-level citations.
- Improved retrieval accuracy and relevance.
- Configurable company knowledge bases.
- Conversation history and follow-up questions.
- Authentication and role-based access control.
- Automated RAG evaluation and performance monitoring.
- Cloud deployment and scalable document processing.

These are potential enhancements and should not be considered implemented features unless they are added to the codebase.

## 👨‍💻 Author

**Prajwal Sortur**

- GitHub: [@prajwalsortur](https://github.com/prajwalsortur)
- Repository: [RAG-Based-Enterprise-Knowledge-Intelligence-System](https://github.com/prajwalsortur/RAG-Based-Enterprise-Knowledge-Intelligence-System)

Interested in building AI/ML applications, Generative AI systems, and data-driven solutions.

---

⭐ If you find this project interesting, consider starring the repository.

