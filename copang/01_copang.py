import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

def getPageString(url):
    data = requests.get(url)
    bsObj = BeautifulSoup(data.content, "html.parser")

    print(bsObj)

    return data.content

url ="https://www.coupang.com/np/categories/413812?channel=home_C1&from=home_C1&traid=home_C1&trcid=102137"

print(getPageString(url))