import requests
from bs4  import BeautifulSoup

def getPageString(url):
    data = requests.get(url)

