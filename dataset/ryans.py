import requests
from bs4 import BeautifulSoup
from csv import writer

# Send a GET request to the website
url = 'https://www.ryanscomputers.com/category/laptop-all-laptop?limit=5&osp=0'
response = requests.get(url)

output_file = open('dataset\\ryans.csv', 'w')


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the href links in the product descriptions
laptop_links = []
for laptop in soup.find_all('p', class_='card-text p-0 m-0 list-view-text'):
    laptop_link = laptop.find('a')['href']

    laptop_response = requests.get(laptop_link)
    laptop_html = laptop_response.text
    laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

    # Extract the laptop name, price, and specifications
    name = laptop_soup.find('span', class_='att-value context').text + '\n'
    output_file.write(name)
    print(name)