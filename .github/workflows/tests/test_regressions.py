from agents.log_analyzer_agent import analyze_log_content

def test_known_error():
    log = open("logs/sample_log1.txt").read()
    result = analyze_log_content(log)
    assert "fix" in result.lower()
