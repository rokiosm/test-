url = "https://news.naver.com/"
html = urlopen(url)
headers = {'User-Agent': 'Mozilla/5.0'}
bs_obj = bs4.BeautifulSoup(html.read(),"html.parser")

ul = bs_obj.find("ul", {"id":"today_main_news"})
print(ul)