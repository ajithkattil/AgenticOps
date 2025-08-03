from tools.log_parser import extract_errors
from retriever.kb_ingest import search_kb

def analyze_log_content(log_text):
    errors = extract_errors(log_text)
    if not errors:
        return "No clear error patterns found in the log."

    kb_response = search_kb(errors)
    return f"Detected Errors:\n{errors}\n\nSuggested Fixes:\n{kb_response}"
