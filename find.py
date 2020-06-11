import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/blog/blog.html')
soup = BeautifulSoup(resp.text, 'html.parser')

# 取得各篇 blog 的所有文字
divs = soup.find_all('div', 'content')
for div in divs:
    print(div.text) # 方法一，使用 .text (會包含許多換行符號)