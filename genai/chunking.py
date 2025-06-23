# placement_chatbot_app/genai/chunking.py
def chunk_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return [text[i:i+500] for i in range(0, len(text), 500)]
