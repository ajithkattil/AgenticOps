from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
import os

def build_vectorstore(vectorstore_path):
    loader = TextLoader("retriever/kb/devops_kb.txt")
    documents = loader.load()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(vectorstore_path)

def search_kb(query, vectorstore_path="/tmp/vectorstore"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(
        vectorstore_path,
        embeddings,
        allow_dangerous_deserialization=True  # ✅ Add this line
    )
    docs = vectorstore.similarity_search(query, k=2)
    return "\n\n".join([doc.page_content for doc in docs])
