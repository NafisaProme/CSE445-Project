import fitz
from docx import Document

from urllib.request import urlopen

import requests, PyPDF2
from PIL import Image
import pytesseract
from io import BytesIO
from bs4 import BeautifulSoup

def read_pdf_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        pdf_content = response.content
        doc = fitz.open("pdf", pdf_content)
        text = ""
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            text += page.get_text()
        print(text)
    else:
        print("Error: Unable to download the PDF.")



def read_docx_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        docx_content = response.content
        doc = Document(BytesIO(docx_content))
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        print(text)
    else:
        print("Error: Unable to download the DOCX file.")

def read_txt_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        txt_content = response.text
        print(txt_content)
    else:
        print("Error: Unable to download the TXT file.")


def read_html(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)
    return text

docx_url = "https://www.mtsac.edu/webdesign/accessible-docs/word/example03.docx"
pdf_url = "https://www.africau.edu/images/default/sample.pdf"
txt_url = "https://filesamples.com/samples/document/txt/sample3.txt"
html_url = "http://www.northsouth.edu/"

read_html(html_url)