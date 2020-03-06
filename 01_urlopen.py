import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

URL = 'http://www.naver.com'
res = requests.get(URL, headers=headers)
soup = BeautifulSoup(res.text)
print(soup)