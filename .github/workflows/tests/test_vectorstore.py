# tests/test_vectorstore.py

"""
Test ingestion of a sample text file and verify vectorstore search works.
"""

import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader

def test_vectorstore_build():
    loader = TextLoader("retriever/kb/devops_kb.txt")
    docs = loader.load()
    assert len(docs) > 0

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    results = db.similarity_search("CI/CD error", k=1)
    assert len(results) > 0
