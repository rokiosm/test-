from libs.stringGetter import getPageString
from bs4 import BeautifulSoup
from libs.coupang.ProductsParser import getProducts

url = "https://www.coupang.com/np/categories/186764"
pageString = getPageString(url)
print(getProducts(pageString))
