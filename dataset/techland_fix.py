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
headings = ['Price', 'Brand', 'Processor', 'Processor Brand', 'Processor Model', 'Generation', 'RAM']

with open('dataset/techland.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for laptop in soup.find_all('div', class_='name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        heading = laptop_soup.find_all('td', class_='attribute-name')

        leave = ['Memory']
        for head in heading:
            if head.text not in leave:
                headings.append(head.text)

    headings = list(dict.fromkeys(headings))
    thewriter.writerow(headings)
    print(headings)
    print(len(headings))

with open('dataset/techland.csv', 'a', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for page_num in range(1, 14):
        # changing the urls of each page accordingly
        url = "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?limit=100&page=" + str(page_num)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for laptop in soup.find_all('div', class_='name'):
            laptop_link = laptop.find('a')['href']
            laptop_links.append(laptop_link)

            laptop_response = requests.get(laptop_link)
            laptop_html = laptop_response.text
            laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

            # scraping the cost of the laptop 
            price = laptop_soup.find('tr')
            cost = price.text.strip()[13:-1]
            
            final_cost = ''
            for i in cost:
                if i != ',':
                    final_cost += i

            # getting the laptop brand
            brand = laptop_soup.find('div', class_='title page-title')
            brand = brand.text.split(' ')[0]
            print(brand)

            heading = laptop_soup.find('div', class_='table-responsive')
            heading_map = dict(zip(headings, ["NULL"] * len(headings)))

            if heading != None:
                lists = heading.find_all('tr')
                for item in lists:
                    take_head = item.find('td', class_='attribute-name')
                    take_name = item.find('td', class_='attribute-value')
                    if take_name != None:
                        x = take_head.text
                        y = take_name.text

                        if x == 'Processor':
                            if 'Intel' in y:
                                heading_map[headings[2]] = y
                            else:
                                pro_brand = y.split(' ')[0]
                                pro_model = y.split(' ')[1] + ' ' + y.split(' ')[2]
                                pro_gen = y.split(' ')[3][0] + 'th Gen'

                                heading_map[headings[2]] = y
                                heading_map[headings[3]] = pro_brand
                                heading_map[headings[4]] = pro_model
                                heading_map[headings[5]] = pro_gen
                        
                        elif x == 'Memory':
                            y = y.split(' ')[0]
                            heading_map[headings[6]] = y
                        
                        elif x == 'Storage':
                            y = y.split(' ')[0]
                            if 'GB' not in y:
                                y += 'GB SSD'
                            else:
                                y += ' SSD'
                            heading_map[x] = y

                        else:
                            heading_map[x] = y

                heading_map['Price'] = final_cost
                heading_map['Brand'] = brand

                info = []
                for heads in headings:
                    info.append(heading_map[heads])
                print(info)
                thewriter.writerow(info)
