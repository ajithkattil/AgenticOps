from difflib import get_close_matches

# Common DevOps keywords for fuzzy matching
KNOWN_TERMS = [
    "kubernetes", "docker", "kubectl", "helm", "terraform",
    "pip", "bash", "cd", "python", "error", "exception", "ci", "jenkins"
]

# Helper to correct minor spelling errors
def correct_input(text):
    words = text.strip().split()
    corrected = []
    for word in words:
        match = get_close_matches(word.lower(), KNOWN_TERMS, n=1, cutoff=0.7)
        corrected.append(match[0] if match else word)
    return " ".join(corrected)

# Classify input as keyword vs full log
def classify_input_type(text):
    if len(text.strip()) < 10:
        return "empty"
    elif len(text.strip().splitlines()) < 2 and len(text.strip().split()) <= 3:
        return "keyword"
    return "log"

# Main agent entrypoint
def analyze_log_content(content):
    input_type = classify_input_type(content)

    if input_type == "empty":
        return "⚠️ Please provide a longer or more detailed log snippet."

    if input_type == "keyword":
        corrected = correct_input(content)
        if corrected != content:
            return f"🔍 Did you mean **'{corrected}'**?\n\nPlease paste related logs or describe the issue in more detail."
        else:
            return f"🤔 The input '{content}' is too short to analyze.\nPlease provide logs or a few lines of error output for better results."

    # === Standard log analysis starts here ===
    # Add your actual RAG + LLM agent logic here
    try:
        if "error" in content.lower() or "exception" in content.lower():
            return (
                "❗ Detected an error pattern. The issue appears to be related to a missing dependency or runtime failure.\n\n"
                "💡 Suggestion: Double-check your environment and dependency versions."
            )
        elif "kubectl" in content.lower() and "not found" in content.lower():
            return (
                "🚫 'kubectl' command not found.\n\n"
                "💡 Suggestion: Ensure the Kubernetes CLI is installed and available in your PATH."
            )
        else:
            return "⚠️ No clear error patterns found in the log. Try uploading a longer or more complete log file."
    except Exception as e:
        return f"❌ Agent failed to analyze log: {str(e)}"
