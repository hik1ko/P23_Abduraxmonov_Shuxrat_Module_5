from httpx import get
from pprint import pprint
from bs4 import BeautifulSoup

response = get('https://www.fitnessblender.com/').text
soup = BeautifulSoup(response, 'html.parser')
rows = soup.find_all('div', {'class': 'group'})[1]
pprint(rows)
