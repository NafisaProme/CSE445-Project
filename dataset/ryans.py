import requests
from bs4 import BeautifulSoup

url = 'https://www.ryanscomputers.com/category/laptop-all-laptop'
r = requests.get(url)

print(r.text)