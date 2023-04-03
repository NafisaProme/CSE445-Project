import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = 'https://www.ryanscomputers.com/category/laptop-all-laptop?limit=2&osp=0'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the href links in the product descriptions
with open('dataset/ryans.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for laptop in soup.find_all('p', class_='card-text p-0 m-0 list-view-text'):
        laptop_link = laptop.find('a')['href']

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        # Extract the laptop name, price, and specifications
        heading = laptop_soup.find_all('span', class_='att-title context')
        detail = laptop_soup.find_all('span', class_='att-value context')

        for head, body in zip(heading, detail):
            info = [head.text, body.text]
            wr.writerow(info)
            
with open('dataset/ryans.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for laptop in soup.find_all('p', class_='card-text p-0 m-0 list-view-text'):
        laptop_link = laptop.find('a')['href']

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        # Extract the laptop name, price, and specifications
        heading = laptop_soup.find_all('span', class_='att-title context')
        detail = laptop_soup.find_all('span', class_='att-value context')

        for head, body in zip(heading, detail):
            info = [head.text, body.text]
            wr.writerow(info)
