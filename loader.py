import os
import fitz  # PyMuPDF
from bs4 import BeautifulSoup
import requests


def load_pdf(file_path):
    doc = fitz.open(file_path)
    texts = []
    for page in doc:
        text = page.get_text()
        texts.append(text)
    return "\n".join(texts)


def load_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)