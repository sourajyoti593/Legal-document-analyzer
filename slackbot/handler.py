from app.query_handler import answer_query

def handle_query(query):
    if "summarize" in query.lower():
        return "(summarization logic here...)"
    return answer_query(query)
