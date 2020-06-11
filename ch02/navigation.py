import requests
from bs4 import BeautifulSoup

resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
soup = BeautifulSoup(resp.text, 'html.parser')

prices = [] # 儲存課程價錢的list

### 取得所有課程售價 ###
# 方法一：使用index
"""
rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
    price = row.find_all('td')[2].text
    prices.append(int(price))
"""

# 方法二：<a> 的 aprent(<td>) 的 previous_sibling
"""
links = soup.find_all('a')
for link in links:
    price = link.parent.previous_sibling.text
    prices.append(int(price))

print(sum(prices) / len(prices))
"""


### 取得每一列所有欄位資訊：find_all('td') or row.children ###
"""
rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
    # 方法一
#    all_tds = row.find_all('td')
    # 方法二
    all_tds = [td for td in row.children]

    # 取得 href 屬性前先檢查其是否存在
    if 'href' in all_tds[3].a.attrs:
        href = all_tds[3].a['href']
    else:
        href = None

    print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])
"""

### 取得每一列所有欄位資訊：stripped_strings ###
rows = soup.find('table', 'table').tbody.find_all('tr')
for row in rows:
    print([s for s in row.stripped_strings])

