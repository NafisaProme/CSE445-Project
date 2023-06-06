# import pandas as pd
# laptop = pd.read_csv('dataset/ryans.csv', encoding='cp1252', on_bad_lines='skip', usecols=['Brand', 'Model', 'Processor Brand'])
# print(laptop)
# Features to choose - Price, Brand,Processor Brand, Processor Type, Processor Generation, Processor Core, RAM size, RAM Type, Total RAM Slot, Max RAM size, Storage(HDD, SSD), Graphics Chipset, Graphics Memory(Shared/Dedicated), Screen size, Display Resolution, USB Ports, LAN supported, WiFi, Bluetooth, WebCam, Keyboard Layout, Color, Weight (Kg), Battery Capacity, Battery Type, Backup Time, Power Adapter, Warranty, Made in

from bs4 import BeautifulSoup
import requests
from csv import writer

# to get access to the website
url = "https://www.startech.com.bd/laptop-notebook/laptop?limit=4&page=1"
# request to the website
page = requests.get(url)


# create an object
soup = BeautifulSoup(page.content, 'html.parser')
laptop_links = []
headings = ['Price', 'Brand']

cnt = 1
with open('dataset/copy.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for laptop in soup.find_all('h4', class_='p-item-name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        heading = laptop_soup.find_all('td', class_='name')

        if cnt >= 3:
            for head in heading:
                headings.append(head.text)
        
        cnt += 1
    thewriter.writerow(headings)

headings = list(dict.fromkeys(headings))
print(len(headings))

with open('dataset/copy.csv', 'a', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for page_num in range(1,4):
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

                # scraping the brand name
                brand = laptop_soup.find('h1', class_='product-name')
                brand_name = brand.text.split()[0]
                info.append(brand_name)

                heading = laptop_soup.find('div', class_='short-description')
                body = heading.find('ul')
                ans = body.find_all('li')

                # for item in ans:
                #     name = item.text
                #     if "Model: " in name:
                #         info.append(name[7:])

                heading = laptop_soup.find_all('td', class_='name')
                lists = laptop_soup.find_all('div', class_='product-details content')

                for list in lists:
                    num = list.find_all('td', class_='value')
                    ind = 2

                    for data in range(len(num)):
                        x = headings[ind]
                        y = heading[data].text.strip()

                        # checking whether the headings match, to decide whether to add the value or the NULL value
                        if x == y:
                            info.append(num[data].text.strip())
                        else:
                            while x != y:
                                ind += 1
                                if ind >= len(headings):
                                    break
                                x = headings[ind]
                                info.append("NULL")
                            
                            info.append(num[data].text.strip())

                        ind += 1
                        if ind >= len(headings):
                            break

                    thewriter.writerow(info)
