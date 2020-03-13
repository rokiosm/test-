import urllib.request
import bs4

url = "https://media.daum.net/economic/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

div = bs_obj.find("div", {"class": "section_cate section_headline"})
lis = div.findAll("a", {"class": "tit_mainnews"})

for li in lis:
    print(li.text)
