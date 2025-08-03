def extract_errors(log_text):
    lines = log_text.splitlines()
    error_lines = [line for line in lines if "ERROR" in line or "Exception" in line]
    return "\n".join(error_lines[:10])  # Return top 10 error lines
