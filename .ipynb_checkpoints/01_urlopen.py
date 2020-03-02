import urllib.request
import  ssl

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

print(html)
context = ssl._create_unverified_context()

