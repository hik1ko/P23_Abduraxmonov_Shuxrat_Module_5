import httpx
from bs4 import BeautifulSoup


def beautiful_soup(link: str):
    response = httpx.get(link)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup
