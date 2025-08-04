# tests/test_artifact_hash.py

"""
Test that FAISS index builds are deterministic.
"""

import hashlib
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader

def hash_faiss_index(index):
    serialized = index.serialize_to_bytes()
    return hashlib.md5(serialized).hexdigest()

def test_artifact_determinism():
    loader = TextLoader("retriever/kb/devops_kb.txt")
    docs = loader.load()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    index1 = FAISS.from_documents(docs, embeddings)
    index2 = FAISS.from_documents(docs, embeddings)

    hash1 = hash_faiss_index(index1)
    hash2 = hash_faiss_index(index2)

    assert hash1 == hash2, "FAISS index builds are not deterministic"

