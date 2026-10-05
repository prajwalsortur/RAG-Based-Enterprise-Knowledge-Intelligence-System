# This file was created to handle document loading for our RAG system.
# It is used to open PDF documents and extract their text.
# The extracted text will later be sent to the text chunking stage.
#
# Connection with other files:
# document_loader.py → text_splitter.py → embeddings.py → vector_store.py
# This keeps document loading separate from the other RAG responsibilities.

import pymupdf


def load_pdf(file_path):
    """
    Open a PDF file and extract all text from its pages.

    Args:
        file_path: Path to the PDF document.

    Returns:
        The complete text extracted from the PDF.
    """

    # Open the PDF document.
    document = pymupdf.open(file_path)

    # Store text extracted from each page.
    text = ""

    # Go through every page in the PDF.
    for page in document:
        text += page.get_text()

    # Close the PDF after extracting the text.
    document.close()

    # Return the complete extracted text.
    return text