An Interactive PDF Chatbot Using Semantic Embeddings and FAISS-Based Vector Search
Team Info
22471A05M0 — D. Satish Babu
Work Done: FAISS indexing, similarity search, performance evaluation

22471A05M8 — K. V. S. N. S. Ashok Kumar
Work Done: Generative model integration (FLAN-T5-XL), response generation

21471A05Q2 — R. Chandara Sekhar
Work Done: Web interface, deployment, documentation

Abstract

The rapid growth of digital documents has created a demand for intelligent retrieval systems that move beyond traditional keyword-based search. This project presents an interactive PDF chatbot that enables users to query PDF documents using natural language. The system integrates semantic embeddings generated using Sentence-BERT, FAISS-based vector similarity search for efficient retrieval, and the FLAN-T5-XL generative model for context-aware answer generation. Unlike conventional approaches, the proposed system retrieves information based on semantic relevance rather than keyword overlap, producing accurate and coherent responses. Experimental evaluation demonstrates improved semantic similarity, reduced response time, and enhanced usability for document-intensive tasks.

Paper Reference (Inspiration)

👉 [An Interactive PDF Chatbot Using Semantic Embeddings and FAISS-Based Vector Search](Paper URL here)
IEEE / Conference paper used as the base reference for the project implementation.

Our Improvement Over Existing Paper

Integrated semantic retrieval and generative response in a unified pipeline

Improved contextual accuracy using overlapping text chunking

Faster response time through optimized FAISS indexing

Zero-shot capability without task-specific fine-tuning

User-friendly web interface for non-technical users

About the Project

What the project does:
Allows users to upload PDF documents and ask questions in natural language to receive precise, context-aware answers.

Why it is useful:
Eliminates manual searching through large PDFs and improves information accessibility for researchers, students, and professionals.

Workflow:
PDF Upload → Text Extraction → Preprocessing → Embedding Generation → FAISS Vector Search → Answer Generation → User Response

Dataset Used

👉 PDF Documents (User-Uploaded)

Dataset Details:

Format: PDF

Source: User-uploaded documents

Text extraction: PyMuPDF (fitz)

Chunking: Sliding window with overlap

Dependencies Used

Python

PyMuPDF (fitz)

SentenceTransformers

FAISS

Transformers (FLAN-T5-XL)

NumPy

Gradio

EDA & Preprocessing

Text extraction from PDF pages

Lowercasing and whitespace normalization

Punctuation removal and tokenization

Lemmatization for word normalization

Replacement of numerical tokens

Sliding-window chunking with 50% overlap

Model Training Info

This system does not require model training.

Embeddings generated using all-MiniLM-L6-v2 SentenceTransformer

Retrieval performed using FAISS approximate nearest neighbor search

Answer generation handled by FLAN-T5-XL (instruction-tuned LLM)

Zero-shot inference without fine-tuning

Model Testing / Evaluation

Semantic similarity (cosine similarity)

Top-K retrieval accuracy

Response latency

Qualitative evaluation of generated answers

Results

Average cosine similarity: ~0.85

Top-3 retrieval accuracy: >90%

Reduced response time compared to baseline chatbot

Improved contextual relevance and answer coherence

Limitations & Future Work

Limitations:

Occasional hallucinations for ambiguous queries

Limited handling of complex tables and figures

English-only support

Future Work:

Domain-specific fine-tuning

Multilingual document support

OCR and multimodal PDF handling

Cloud-based scalable deployment

Feedback-based adaptive learning

Deployment Info

Implemented as a web application using Gradio

Runs on CPU/GPU systems

Can be extended to Flask/FastAPI for production deployment

