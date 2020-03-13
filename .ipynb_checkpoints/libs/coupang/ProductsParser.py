from bs4 import BeautifulSoup

def getProduct(li):
    img = li.find("dt", {"class", "image"}).find("img")
    print(img)
    return {}

def getProducts(string):
        ul = bsObj.find("ul", {"id": "productList"})
        lis = ul.findAll("li")
        li = lis[1]
        print(li)
        return []

url = "https://www.coupang.com/np/categories/186764"
PageString = getPageString(url)
print(getProducts(PageString))

