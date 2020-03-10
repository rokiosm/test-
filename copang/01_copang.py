import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

# 스킨케어 - 쿠팡랭킹순 모든 상품,가격 가져오기
for idx in range(1, 17):
    url = "http://www.coupang.com/np/categories/176860?page=" + str(idx)

    print(url)
    result = requests.get(url, headers=headers)
    soup_obj = BeautifulSoup(result.content, "html.parser")

    div = soup_obj.findAll("div", {"class": "name"})
    lis = soup_obj.find("ul", {"id": "productList"}).findAll("li")

    for li in lis:
        product = li.find("div", {"class": "name"})
        price = li.find("em", {"class": "sale"}).find(
            "strong", {"class": "price-value"}
        )
        print("화장품명: " + product.text.strip() + " / " + "상품가격: " + price.text.strip())