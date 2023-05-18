from bs4 import BeautifulSoup
import requests
from csv import writer

# to get access to the website

url = "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?limit=100&page=1"
# request to the website
page = requests.get(url)


# create an object
soup = BeautifulSoup(page.content, 'html.parser')
laptop_links = []

with open('dataset/techland.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for laptop in soup.find_all('div', class_='name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        heading = laptop_soup.find_all('td', class_='attribute-name')
        info = []
        info.append('Price')

        for head in heading:
            info.append(head.text)

        thewriter.writerow(info)
        break

with open('dataset/techland.csv', 'a', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for page_num in range(1, 14):
        # changing the urls of each page accordingly
        url = "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?limit=100&page=" + str(page_num)
        page = requests.get(url)
        print(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for laptop in soup.find_all('div', class_='name'):
            laptop_link = laptop.find('a')['href']
            laptop_links.append(laptop_link)

            laptop_response = requests.get(laptop_link)
            laptop_html = laptop_response.text
            laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

            info = []

            # scraping the cost of the laptop 
            price = laptop_soup.find('tr')
            cost = price.text.strip()[13:-1]
            
            final_cost = ''
            for i in cost:
                if i != ',':
                    final_cost += i

            info.append(final_cost)

            heading = laptop_soup.find('div', class_='table-responsive')

            if heading != None:
                lists = heading.find_all('tr')
                for item in lists:
                    take = item.find('td', class_='attribute-value')
                    if take != None:
                        info.append(take.text)

            thewriter.writerow(info)
