import gradio as gr
import os

from agents.log_analyzer_agent import analyze_log_content
from retriever.kb_ingest import build_vectorstore

# Rebuild vectorstore in /tmp (for Hugging Face Spaces)
VECTOR_DB_PATH = "/tmp/vectorstore"
os.makedirs(VECTOR_DB_PATH, exist_ok=True)
build_vectorstore(VECTOR_DB_PATH)

# Sample logs available for dropdown selection
SAMPLE_LOGS = {
    "None": "",
    "GPU Error Log": "sample_logs/gpu_test_error.log",
    "GPU Success Log": "sample_logs/gpu_test_success.log"
}

# Unified handler for text, file, or dropdown
def handle_input(text_input, file_input, sample_log_key):
    content = ""

    if sample_log_key and sample_log_key != "None":
        try:
            with open(SAMPLE_LOGS[sample_log_key], "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            return f"❌ Failed to read sample log: {str(e)}"

    elif file_input:
        try:
            with open(file_input.name, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            return f"❌ Failed to read uploaded file: {str(e)}"

    elif text_input:
        content = text_input.strip()

    if not content:
        return "⚠️ Please provide a log input (upload file, paste text, or choose sample log)."

    return analyze_log_content(content)

# UI Layout
iface = gr.Interface(
    fn=handle_input,
    inputs=[
        gr.Textbox(lines=8, label="Paste Log Text (Optional)"),
        gr.File(label="Upload Log File (Optional)"),
        gr.Dropdown(choices=list(SAMPLE_LOGS.keys()), label="Or Select Sample Log", value="None")
    ],
    outputs="text",
    title="AgenticOps – DevOps + GPU CI Log Analyzer",
    description="Paste CI logs (e.g., from Jenkins, PyTorch, CUDA), upload a file, or select a sample log to simulate failure/success. Agentic AI will analyze and suggest fixes."
)

if __name__ == "__main__":
    iface.launch()
