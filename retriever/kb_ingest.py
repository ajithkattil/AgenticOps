def search_kb(query):
    # Simulate RAG result
    if "NullPointerException" in query:
        return "This error usually occurs due to uninitialized objects. Check your object references."
    elif "OOMKilled" in query:
        return "This container was OOMKilled. Increase memory limits or optimize your application."
    else:
        return "No matching KB entries found. Consider updating the KB."
