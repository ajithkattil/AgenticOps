import os

def analyze_log(log_text):
    """
    Enhanced analyzer that detects error patterns case-insensitively.
    """
    text = log_text.lower()

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
    """
    Test that verifies known Jenkins log with NullPointerException is flagged correctly.
    """
    # Ensure directory and file exist
    os.makedirs("tests/sample_logs", exist_ok=True)
    log_path = "tests/sample_logs/jenkins_null_pointer.txt"

    # Create the sample log file dynamically to avoid CI issues
    log_content = """Started by user Jane Doe
Running as SYSTEM
[Pipeline] stage
[Pipeline] { (Deploy)
Deploying application...
ERROR: java.lang.NullPointerException at line 45
Jenkins build failed due to a NullPointerException in CpsThreadGroup.java
[Pipeline] End of Pipeline
Finished: FAILURE
"""
    with open(log_path, "w") as f:
        f.write(log_content)

    # Read and analyze
    with open(log_path, "r") as f:
        log_text = f.read()

    result = analyze_log(log_text)
    print("🧪 Test Output:", result)

    # Ensure expected content is flagged
    assert "NullPointerException" in result or "Jenkins" in result
