import urllib.request
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

print(bs_obj)