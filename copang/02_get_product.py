from libs.StringGetter import getPageString
from bs4 import beautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

def getProducts(string):
    ul = bsObj.find("ul", {"id":"productList"})
    lis = ul.findAll("li")
    li = lis[1]
    print(li)
    return []

url = "https://www.coupang.com/np/categories/186764"
PageString = getPageString(url)
print(getProducts(PageString))
