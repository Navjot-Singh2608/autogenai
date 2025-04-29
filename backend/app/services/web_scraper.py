import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()
