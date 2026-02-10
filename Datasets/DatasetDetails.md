# Dataset Description

## Overview

This project does **not rely on any predefined or static dataset**.  
Instead, it operates on **user-provided documents (PDF or text-based files)** that are dynamically processed at runtime. The dataset is **created on-the-fly** from the uploaded document, making the system flexible, scalable, and domain-independent.

---

## Nature of the Dataset

- **Dataset Type:** Dynamic, document-driven
- **Data Source:** User-uploaded PDF / DOC / TXT files
- **Storage:** In-memory or temporary vector store (no permanent dataset storage)
- **Domain:** Open-domain (depends on the uploaded document)
- **Size:** Varies per document (from a few pages to large multi-page files)

---

## Why No Predefined Dataset Is Used

Traditional Question Answering systems rely on large labeled datasets.  
In contrast, this project follows a **Retrieval-Augmented Generation (RAG)** approach, where:

- The **input document itself acts as the dataset**
- No manual data labeling is required
- The system adapts to any document without retraining

This design ensures:
- High flexibility across domains
- Reduced dependency on external datasets
- Real-time knowledge extraction

---

## Dataset Creation Pipeline

The dataset is generated dynamically using the following steps:

1. **Document Upload**
   - User uploads a PDF or document file.

2. **Text Extraction**
   - Text is extracted using PDF parsers or OCR (for scanned documents).

3. **Text Preprocessing**
   - Removal of noise (headers, footers, symbols)
   - Sentence normalization and cleaning

4. **Text Chunking**
   - Document text is split into semantically meaningful chunks.

5. **Embedding Generation**
   - Each chunk is converted into vector embeddings using a transformer-based model.

6. **Vector Indexing**
   - Embeddings are stored in a vector database for similarity search.

The resulting indexed chunks together form the **effective dataset** for question answering.

---

## Dataset Format

Each dynamically generated dataset consists of:

| Field Name      | Description |
|----------------|------------|
| `chunk_id`     | Unique identifier for each text chunk |
| `content`      | Extracted text content |
| `embedding`    | Vector representation of the text |
| `metadata`     | Page number, section, or source info |

---

## Example Dataset Entry

```json
{
  "chunk_id": "doc_01_chunk_12",
  "content": "This section explains the architecture of the proposed system...",
  "embedding": [0.021, -0.334, 0.876, ...],
  "metadata": {
    "page_number": 5,
    "source": "uploaded_document.pdf"
  }
}
