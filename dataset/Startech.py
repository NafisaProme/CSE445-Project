from bs4 import BeautifulSoup
import requests
from csv import writer

# to get access to the website

url = "https://www.startech.com.bd/laptop-notebook/laptop?limit=90&page=1"
# request to the website
page = requests.get(url)


# create an object
soup = BeautifulSoup(page.content, 'html.parser')
laptop_links = []

with open('dataset/startech.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for laptop in soup.find_all('h4', class_='p-item-name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        heading = laptop_soup.find_all('td', class_='name')
        info = []
        info.append('Price')

        for head in heading:
            info.append(head.text)

        thewriter.writerow(info)
        break

with open('dataset/startech.csv', 'a', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for page_num in range(1,9):
        url = url[:-1]
        url = url + str(page_num)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for laptop in soup.find_all('h4', class_='p-item-name'):
            laptop_link = laptop.find('a')['href']
            laptop_links.append(laptop_link)

            laptop_response = requests.get(laptop_link)
            laptop_html = laptop_response.text
            laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

            info = []
        
            price = laptop_soup.find('td', class_='product-info-data product-regular-price')
            if price != None:

                for cost in price:
                    work = cost.text
                    name = ''
                    for i in work:
                        if i != ',' and i != '৳':
                            name = name + i
                         
                    info.append(name)
                
                heading = laptop_soup.find('div', class_='short-description')
                body = heading.find('ul')
                ans = body.find_all('li')

                
                for item in ans:
                    name = item.text
                    if "Model: " in name:
                        info.append(name[7:])
            
                lists = laptop_soup.find_all('div', class_='product-details content')
                        
                for list in lists:
                    num = list.find_all('td', class_='value')
                    for i in num:
                        info.append(i.text)
                    
                
                thewriter.writerow(info)