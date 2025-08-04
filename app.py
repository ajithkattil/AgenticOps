import gradio as gr
import sys, os

# Ensure internal modules are accessible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.log_analyzer_agent import analyze_log_content
from retriever.kb_ingest import build_vectorstore

# Rebuild vectorstore in /tmp for Hugging Face Spaces
VECTOR_DB_PATH = "/tmp/vectorstore"
os.makedirs(VECTOR_DB_PATH, exist_ok=True)
build_vectorstore(VECTOR_DB_PATH)

# Unified handler for file + text
def handle_input(text_input, file_input):
    content = ""

    if file_input:
        try:
            with open(file_input.name, "r", encoding="utf-8") as f:
                content += f.read()
        except Exception as e:
            return f"❌ Failed to read file: {str(e)}"

    if text_input:
        content += "\n" + text_input.strip()

    if not content.strip():
        return "⚠️ Please provide a log file or paste some log content."

    result = analyze_log_content(content)
    return result

# Gradio interface
iface = gr.Interface(
    fn=handle_input,
    inputs=[
        gr.Textbox(lines=10, label="Paste Log Text (Optional)"),
        gr.File(label="Upload Log File (Optional)")
    ],
    outputs="text",
    title="AgenticOps – DevOps Log Analyzer (Hugging Face)",
    description="Paste DevOps logs or upload a .txt file. Agentic AI will analyze the error and suggest a fix using LLM + RAG."
)

if __name__ == "__main__":
    iface.launch()
