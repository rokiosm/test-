import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

def getPageString(url):
    data = requests.get(url)
    bsObj = BeautifulSoup(data.content, "html.parser")

    print(bsObj)

    return data.content