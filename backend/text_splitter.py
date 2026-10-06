"""
Text Chunking Module

Why this file was created:
This file handles the text chunking stage of our RAG system.

What it is used for:
It takes text extracted from documents and divides it into
smaller chunks that can later be converted into embeddings
and stored in a vector database.

How it connects:
document_loader.py extracts text from the PDF.
This file receives that extracted text and creates chunks.
The chunks will later be used by the embedding and retrieval stages.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


# These settings control how large each chunk is and
# how much text is shared between neighboring chunks.
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def split_text(text: str) -> list[str]:
    """
    Split extracted document text into smaller chunks.

    Args:
        text: Text extracted from a document.

    Returns:
        A list containing the generated text chunks.
    """

    # RecursiveCharacterTextSplitter tries to keep related
    # text together while splitting large text into smaller pieces.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    return splitter.split_text(text)