import gradio as gr
from agents.log_analyzer_agent import analyze_log_content

def handle_file_upload(file):
    content = file.read().decode("utf-8")
    return analyze_log_content(content)

iface = gr.Interface(
    fn=handle_file_upload,
    inputs=gr.File(label="Upload Log File"),
    outputs="text",
    title="AgenticOps – Log Analyzer",
    description="Upload a Jenkins or Kubernetes log file and let the AgenticOps AI analyze it."
)

if __name__ == "__main__":
    iface.launch()
