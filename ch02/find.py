import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/blog/blog.html')
soup = BeautifulSoup(resp.text, 'html.parser')

# 取得各篇 blog 的所有文字
divs = soup.find_all('div', 'content')
for div in divs:
#   方法一：使用 .text (會包含許多換行符號)
#    print(div.text)
#   方法二：使用tag定位
#    print(div.h6.text.strip(), div.h4.text.strip(), div.p.text.strip())
#   方法三：使用 .stripped_strings
    print([s for s in div.stripped_strings])


