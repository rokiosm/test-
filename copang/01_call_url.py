import  requests
from bs4 import BeautifulSoup

def getPageString(url):
    data = requests.get(url)
    bsObj = BeautifulSoup(data.content, "html.parser")

    print(bsObj)

    return data.content

url = "https://www.coupang.com/np/categories/186764"

print(getPageString(url))

