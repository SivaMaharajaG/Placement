# placement_chatbot_app/websearch/browser.py
import requests
from bs4 import BeautifulSoup

def fetch_results(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.get_text()[:1000]
