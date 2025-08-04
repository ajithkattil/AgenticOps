# tests/test_logs_regression.py

"""
Run known error logs through the pipeline and check output contains expected keywords.
"""

from agents.log_analyzer_agent import analyze_log_content

def test_log_regression_known_case():
    with open("tests/sample_logs/jenkins_null_pointer.txt", "r") as f:
        log = f.read()

    response = analyze_log_content(log)
    assert "NullPointerException" in response or "Jenkins" in response

