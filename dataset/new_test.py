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
headings = ['Price', 'Brand']

with open('dataset/Startech.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for laptop in soup.find_all('h4', class_='p-item-name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        heading = laptop_soup.find_all('td', class_='name')

        for head in heading:
            headings.append(head.text)

    headings = list(dict.fromkeys(headings))
    thewriter.writerow(headings)
    print(len(headings))

with open('dataset/Startech.csv', 'a', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for page_num in range(1, 9):
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

            price = laptop_soup.find('td', class_='product-info-data product-regular-price')
            if price != None:

                for cost in price:
                    work = cost.text
                    name = ''
                    for i in work:
                        if i != ',' and i != '৳':
                            name = name + i

                laptop_cost = name

                # scraping the brand name
                brand = laptop_soup.find('h1', class_='product-name')
                brand_name = brand.text.split()[0]

                heading = laptop_soup.find_all('td', class_='name')
                lists = laptop_soup.find_all('div', class_='product-details content')

                for list in lists:
                    num = list.find_all('td', class_='value')

                    heading_map = dict(zip(headings, ["NULL"] * len(headings)))

                    # mapping the properties to the values
                    for data in range(len(num)):
                        x = heading[data].text.strip()
                        y = num[data].text.strip()

                        if x == "Processor Model":
                                y = y.split("-")[0]
                        
                        heading_map[x] = y

                    heading_map["Price"] = laptop_cost
                    heading_map["Brand"] = brand_name

                    # inserting the mapped values into the list, and writing them to the csv file 
                    info = []
                    for heads in headings:
                        info.append(heading_map[heads])

                    thewriter.writerow(info)