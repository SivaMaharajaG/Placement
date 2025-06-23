# placement_chatbot_app/genai/vectorizer.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()

def get_most_relevant_chunk(query, chunks):
    vectors = vectorizer.fit_transform([query] + chunks)
    sims = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return chunks[sims.argmax()]
