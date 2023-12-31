import requests
from bs4 import BeautifulSoup
from csv import writer
import re

# Send a GET request to the website
url = "https://www.globalbrand.com.bd/all-laptop?limit=5"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
laptop_links=[]
headings = ['Price']

with open('dataset/copy.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for laptop in soup.find_all('div', class_='name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        heading1 = laptop_soup.find_all('td')
        
        for head in heading1:
            take = head.text 
            if ':' in take:
                take = take.split(':')[0]
                headings.append(take)
                
    headings = list(dict.fromkeys(headings))
    thewriter.writerow(headings)
    print(headings)
    print(len(headings))

# with open('dataset/copy.csv', 'a', encoding='utf8', newline='') as f:
#     thewriter = writer(f)



#     for laptop in soup.find_all('div', class_='name'):
#         laptop_link = laptop.find('a')['href']
#         laptop_links.append(laptop_link)

#         laptop_response = requests.get(laptop_link)
#         laptop_html = laptop_response.text
#         laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

#         info = []
        
#         price = laptop_soup.find('div', class_='product-price')
#         if price != None:

#             for cost in price:
#                 work = cost.text
#                 name = ''
#                 for i in work:
#                     if i != ',' and i != '৳':
#                         name = name + i
                         
#                 info.append(name)
       
#         lists = laptop_soup.find_all('table', class_="table table-bordered")
                
#         for list in lists:
#             num = list.find_all('td')
#             for n in num:
#                 text = n.text
#                 if ":" in text:
#                     value = text.split(":")[1].strip()
#                     info.append(value)
       
#         thewriter.writerow(info)
