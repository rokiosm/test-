from bs4 import BeautifulSoup
html = """
<html><head>
<h1>HTML 헤더 부분</h1>
<p> BeautifulSoup 으로</p>
<p> 데이터 추출 하기</p>
</head><body>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.p
p2 = p1.next_sibling.next_sibling

print("h1:", h1.string)
print("p1:", p1.string)
print("p2:", p2.string)

