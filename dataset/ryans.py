import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = 'https://www.ryanscomputers.com/category/laptop-all-laptop?limit=400&osp=0'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# opening the file and writing to it
with open('dataset/ryans.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    headings = ['Price']

    # writing the heading of all the laptops
    for laptop in soup.find_all('p', class_='card-text p-0 m-0 list-view-text'):
        laptop_link = laptop.find('a')['href']

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        # extracting the headings(specifications) of the laptops 
        heading = laptop_soup.find_all('span', class_='att-title context')

        for head in heading:
            headings.append(head.text.strip())

    headings = list(dict.fromkeys(headings))
    wr.writerow(headings)
    print(headings)

    # extracting the specification of all the laptops in the page, viewing the details
    for laptop in soup.find_all('p', class_='card-text p-0 m-0 list-view-text'):
        laptop_link = laptop.find('a')['href']

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')
        
        # picking the price of the laptop 
        price = laptop_soup.find_all('span', class_='rp-block mb-2')
        final_cost = ''
        for data in price:
            take = data.text.strip()        
            cost = take[17:]

            # removing the comma from the price 
            for num in cost:
                if num != ',':
                    final_cost = final_cost + str(num)

            break

        # Extract the laptop name, price, and specifications
        heading = laptop_soup.find_all('span', class_='att-title context')
        detail = laptop_soup.find_all('span', class_='att-value context')

        heading_map = dict(zip(headings, ["NULL"] * len(headings)))

        if len(detail) > 0:
            for data in range(len(detail)):
            # print(data)
                x = heading[data].text.strip()
                y = detail[data].text.strip()
                
                if x == "Generation" and y != "Not Applicable":
                    y = y.split(' ')[0] + " Gen"
                
                elif x == 'Processor Base Frequency':
                    y = y[0:3]
                    print(y)

                elif x == 'Processor Max Turbo Frequency':
                    y = y[0:3]
                    print(y)

                heading_map[x] = y
            
            heading_map['Price'] = final_cost

            info = []
            for heads in headings:
                info.append(heading_map[heads])
            
            print(info)

            wr.writerow(info)
