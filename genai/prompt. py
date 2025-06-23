# placement_chatbot_app/genai/prompt.py
from genai.chunking import chunk_text
from genai.vectorizer import get_most_relevant_chunk

def handle_query(query, username):
    chunks = chunk_text("genai/data/tamilnadu_it_placement_dataset.txt")
    best_chunk = get_most_relevant_chunk(query, chunks)
    response = f"Based on your qualification, here’s what I found:\n\n{best_chunk}"
    return response
