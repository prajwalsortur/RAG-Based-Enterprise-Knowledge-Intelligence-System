# RAG-Based Enterprise Knowledge Intelligence System

An AI-powered knowledge assistant that uses **Retrieval-Augmented Generation (RAG)** to answer questions from enterprise documents. It combines semantic search, vector storage, and a Large Language Model (LLM) to generate context-aware answers through a simple web-based chat interface.

## 🚀 Project Overview

Organizations store important information in documents, policies, manuals, and knowledge bases. Finding specific information manually can be time-consuming.

This project addresses that problem by allowing users to ask questions in natural language and receive answers based on information retrieved from a knowledge base.

The system uses **Python, FastAPI, Sentence Transformers, ChromaDB, Groq, and React** to build an end-to-end RAG application.

## ✨ Key Features

- **PDF Document Loading:** Extracts text from PDF documents.
- **Text Chunking:** Divides extracted text into smaller, manageable chunks.
- **Text Embeddings:** Converts text chunks into numerical vector representations using Sentence Transformers.
- **Vector Database:** Stores and retrieves relevant information using ChromaDB.
- **Semantic Retrieval:** Finds document content relevant to a user's question.
- **LLM Integration:** Uses the Groq API to generate answers from retrieved context.
- **FastAPI Backend:** Exposes an API endpoint for processing user questions.
- **React Frontend:** Provides a user-friendly chat interface.
- **Knowledge-Grounded Responses:** Uses retrieved document content to help keep answers relevant to the knowledge base.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| PyMuPDF | PDF text extraction |
| LangChain Text Splitters | Text chunking |
| Sentence Transformers | Text embedding generation |
| ChromaDB | Vector storage and similarity search |
| Groq API | LLM-powered answer generation |
| FastAPI | Backend API |
| React | Frontend user interface |
| Vite | Frontend development server |
| CSS | Interface styling |
| Git and GitHub | Version control and project hosting |

## 🏗️ System Architecture

```text
             Enterprise PDF Documents
                       |
                       v
              PDF Text Extraction
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
                       v
User Question --> FastAPI Backend
                       |
                       v
                Query Embedding
                       |
                       v
              Relevant Information
                  Retrieval
                       |
                       v
              Retrieved Context
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

1. **Document loading:** The system extracts text from an enterprise PDF document.
2. **Text splitting:** The extracted content is divided into smaller chunks with overlapping text to preserve context.
3. **Embedding generation:** Each chunk is converted into a numerical representation using a Sentence Transformers embedding model.
4. **Vector storage:** The embeddings and associated text are stored in ChromaDB.
5. **Question processing:** A user submits a question through the React chat interface.
6. **Information retrieval:** The backend searches the vector database for relevant document chunks.
7. **Answer generation:** The retrieved context is passed to the Groq-powered LLM to generate a response.
8. **Response display:** FastAPI returns the answer to the frontend, where it is displayed in the chat interface.

## 📁 Project Structure

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
├── .env
├── .gitignore
└── README.md
```

*Note: This structure highlights the main project components. Some generated files and additional configuration files are omitted for readability.*

## ⚙️ Installation and Setup

### Prerequisites

- Python installed
- Node.js and npm installed
- A Groq API key

### 1. Clone the Repository

```powershell
git clone https://github.com/prajwalsortur/RAG-Based-Enterprise-Knowledge-Intelligence-System.git

cd RAG-Based-Enterprise-Knowledge-Intelligence-System
```

### 2. Set Up the Python Environment

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required Python packages:

```powershell
pip install pymupdf langchain-text-splitters sentence-transformers chromadb groq python-dotenv fastapi uvicorn
```

### 3. Configure the API Key

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual API key. Never commit your `.env` file or expose your API key publicly.

### 4. Start the Backend

From the project root, run:

```powershell
uvicorn backend.main:app --reload
```

If the import path does not match your current setup, start the server from the `backend` directory instead:

```powershell
cd backend
uvicorn main:app --reload
```

The API should be available at:

```text
http://127.0.0.1:8000
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

### 5. Start the Frontend

Open a second terminal and navigate to the frontend directory:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL displayed by Vite, usually:

```text
http://localhost:5173
```

Keep the backend and frontend running in separate terminals.

**Configuration note:** The exact startup commands depend on the import paths in your current `main.py` and the API URL configured in your frontend. Use the command matching your project configuration.

## 🔌 API Usage

The FastAPI backend provides a question-answering endpoint.

**Endpoint:** `POST /ask`

Example request body:

```json
{
  "question": "How many paid leave days do employees receive per year?"
}
```

Example response:

```json
{
  "answer": "Employees receive 18 paid leave days per year."
}
```

The answer shown is an example based on the sample knowledge document.

## 🧪 Example Questions

Using the included sample enterprise knowledge document, users can ask questions such as:

- How many paid leave days do employees receive per year?
- What are the company's working hours?
- How many days per week can employees work remotely?
- Which team handles IT support?

The quality of the answers depends on the source documents, retrieved context, embedding model, and LLM response.

## 🎯 Project Objectives

- Build an end-to-end Retrieval-Augmented Generation application.
- Understand document processing and semantic search.
- Connect a vector database with an LLM.
- Develop a REST API using FastAPI.
- Integrate an AI backend with a React frontend.
- Explore practical applications of Generative AI for enterprise knowledge management.

## 🔮 Future Enhancements

Potential improvements include:

- Support for multiple PDF documents and additional file formats.
- Document upload and knowledge-base management.
- Source references for generated answers.
- Improved retrieval accuracy and answer evaluation.
- Conversation history and chat management.
- Authentication and role-based access control.
- Deployment to cloud platforms.

These are planned enhancements, not claims about currently implemented features.

## 👨‍💻 Author

**Prajwal Sortur**

- GitHub: [@prajwalsortur](https://github.com/prajwalsortur)
- Project Repository: [RAG-Based Enterprise Knowledge Intelligence System](https://github.com/prajwalsortur/RAG-Based-Enterprise-Knowledge-Intelligence-System)

