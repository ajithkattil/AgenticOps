import os

def analyze_log(log_text):
    """
    Very basic rule-based analyzer for regression logs.
    You can later replace this with an LLM call or LangChain tool.
    """
    text = log_text.lower()

    # Match common patterns
    if "nullpointerexception" in text and "jenkins" in text:
        return "❌ Detected Jenkins NullPointerException"
    elif "nullpointerexception" in text:
        return "❌ Detected NullPointerException"
    elif "jenkins" in text and "failure" in text:
        return "❌ Jenkins build failed"
    elif "error" in text:
        return "❌ Generic error detected"
    
    return "⚠️ No clear error patterns found in the log. Try uploading a longer or more complete log file."


def test_log_regression_known_case():
    # Ensure test file exists
    log_file_path = "tests/sample_logs/jenkins_null_pointer.txt"
    assert os.path.exists(log_file_path), f"Missing log file: {log_file_path}"

    # Read log content
    with open(log_file_path, "r") as f:
        log_text = f.read()

    # Run analysis
    result = analyze_log(log_text)
    print("🧪 Test Output:", result)  # For CI debugging

    # Assertions (expandable)
    assert "NullPointerException" in result or "Jenkins" in result
