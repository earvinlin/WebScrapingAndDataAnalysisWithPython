import requests
from bs4 import BeautifulSoup

resp = requests.get('https://ts1.chinese.travian.com/login.php')
soup = BeautifulSoup(resp.text, 'html5lib')

# 取得各篇 blog 的所有文字
tables = soup.find_all('table', limit=1)
print(tables[0].tbody.td.name)

a, b = ("100", "5")
print(str(a) + " " + str(b))
