import os

# Load .env only in local dev (Hugging Face Spaces inject secrets directly)
if os.getenv("HF_SPACE_ID") is None:
    from dotenv import load_dotenv
    load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint  # ✅ Updated import
from langchain.schema import HumanMessage
from tools.log_parser import extract_errors
from retriever.kb_ingest import search_kb

# ✅ Updated to use new class
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 512
    }
)

def analyze_log_content(log_text):
    errors = extract_errors(log_text)
    if not errors:
        return "✅ No clear error patterns found in the log."

    kb_summary = search_kb(errors)

    prompt = f"""
You are a DevOps assistant AI. A user uploaded the following error log:

--- Error Log ---
{errors}

--- Internal KB Context ---
{kb_summary}

Analyze the log and provide a root cause and fix suggestion.
"""

    response = llm([HumanMessage(content=prompt)])
    return str(response.content)
