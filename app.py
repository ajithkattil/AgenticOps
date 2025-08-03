import gradio as gr
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.log_analyzer_agent import analyze_log_content
from retriever.kb_ingest import build_vectorstore
import os

# Rebuild vectorstore in /tmp for Hugging Face Spaces
VECTOR_DB_PATH = "/tmp/vectorstore"
os.makedirs(VECTOR_DB_PATH, exist_ok=True)
build_vectorstore(VECTOR_DB_PATH)

def handle_file_upload(file):
    try:
        if isinstance(file, str):  # file is a file path string (NamedString case)
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
        elif hasattr(file, "name"):  # file-like object
            with open(file.name, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            content = str(file)
    except Exception as e:
        return f"❌ Failed to read file: {str(e)}"

    result = analyze_log_content(content)
    return result


iface = gr.Interface(
    fn=handle_file_upload,
    inputs=gr.File(label="Upload Log File"),
    outputs="text",
    title="AgenticOps – DevOps Log Analyzer (Hugging Face)",
    description="Upload Jenkins/Kubernetes logs. Agentic AI will analyze the error and suggest a fix using LLM + RAG."
)

if __name__ == "__main__":
    iface.launch()
