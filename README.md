# RAG-BASED ENTERPRISE KNOWLEDGE INTELLIGENCE SYSTEM

A Retrieval-Augmented Generation (RAG) based system that allows users to ask questions about enterprise documents and receive answers based on the information available in those documents.

## 🎯 Project Objective

The main goal of this project is to build an AI-powered knowledge system that can:

* Load enterprise documents
* Extract and process document content
* Split documents into smaller chunks
* Convert text into embeddings
* Store document embeddings
* Retrieve relevant information for a user's question
* Generate answers using an LLM based on the retrieved information

## 🏗️ RAG Workflow

```text
Enterprise Documents
        ↓
Document Loading
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Text Embeddings
        ↓
Vector Database
        ↓
User Question
        ↓
Similarity Search
        ↓
Relevant Document Chunks
        ↓
LLM
        ↓
Final Answer
```

## 🛠️ Technologies

* Python
* RAG
* Embeddings
* Vector Database
* Large Language Model (LLM)
* FastAPI
* HTML / CSS / JavaScript

## 📁 Project Structure

RAG-BASED-ENTERPRISE-KNOWLEDGE-INTELLIGENCE-SYSTEM/
│
├── data/
│   └── documents/
│       ├── company_policy.pdf
│       ├── employee_handbook.pdf
│       └── ...
│
├── src/
│   ├── document_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## ✨ Features

* 📄 Enterprise document processing
* 🔍 Semantic document search
* 🧠 Context-aware AI responses
* 📚 Knowledge retrieval from uploaded documents
* ⚡ Backend API
* 💬 Question-answering interface

## 🚀 Project Status

## System Architecture

![RAG Architecture](docs/rag-architecture.png)

**Currently in development.**

The system will be built step by step, with each component tested before moving to the next stage.

## 👨‍💻 Author

**Prajwal Sortur**

* Data Science
* AI/ML
* Generative AI
* Data Analytics
* AI Engineering

