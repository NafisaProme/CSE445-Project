import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = 'https://www.ryanscomputers.com/category/laptop-all-laptop?limit=20&osp=0'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# opening the file and writing to it
with open('dataset/ryans.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    # writing the heading of all the laptops
    for laptop in soup.find_all('p', class_='card-text p-0 m-0 list-view-text'):
        laptop_link = laptop.find('a')['href']

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        # Extract the laptop name, price, and specifications
        heading = laptop_soup.find_all('span', class_='att-title context')
        info = []

        for head in heading:
            info.append(head.text.strip())

        wr.writerow(info)
        break

    # writing the properties of each laptop
    for laptop in soup.find_all('p', class_='card-text p-0 m-0 list-view-text'):
        laptop_link = laptop.find('a')['href']

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        # Extract the laptop name, price, and specifications
        detail = laptop_soup.find_all('span', class_='att-value context')
        info = []

        for data in detail:
            info.append(data.text)

        wr.writerow(info)
