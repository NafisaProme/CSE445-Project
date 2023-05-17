import requests
from bs4 import BeautifulSoup
from csv import writer

# Send a GET request to the website
url = "https://www.globalbrand.com.bd/index.php?_route_=laptop/all-laptop&limit=100"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
laptop_links=[]

with open('gbrand.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    for laptop in soup.find_all('div', class_='name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        heading = laptop_soup.find_all('td')
        info = []
        
        for head in heading:
            info.append(head.text)

        thewriter.writerow(info)
        break

    with open('gbrand.csv', 'a', encoding='utf8', newline='') as f:
       thewriter = writer(f)
       for laptop in soup.find_all('div', class_='name'):
        laptop_link = laptop.find('a')['href']
        laptop_links.append(laptop_link)

        laptop_response = requests.get(laptop_link)
        laptop_html = laptop_response.text
        laptop_soup = BeautifulSoup(laptop_html, 'html.parser')

        
       
        lists = laptop_soup.find_all('table', class_="table table-bordered")
                
        for list in lists:
            num = list.find_all('tr')
            for i in num:
                info.append(i.text)
            
       
        thewriter.writerow(info)
