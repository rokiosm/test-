import urllib.request
import bs4


# url = "http://news.naver.com"
url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

div = bs_obj.find("div", {"class": "_persist"})
lis = div.findAll("a", {"class": "cluster_text_headline"})

for li in lis:
    print(li.text)