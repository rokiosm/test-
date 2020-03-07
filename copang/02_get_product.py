from libs.StringGetter import getPageString
from bs4 import beautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

def getProducts(string):

url ="https://www.coupang.com/np/categories/413812?channel=home_C1&from=home_C1&traid=home_C1&trcid=102137"

print(getPageString(url))
