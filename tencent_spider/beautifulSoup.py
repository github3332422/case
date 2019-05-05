from bs4 import BeautifulSoup
import requests

url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=Python'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection':'keep-alive',
    'Cookie': '_ga=GA1.2.1249177683.1539506743; pgv_pvi=5377200128; _gcl_au=1.1.202219451.1547373198; pgv_pvid=1246724880; PHPSESSID=h0rpjpe1vbblr7k9857srgf1j4; pgv_si=s6263471104',
    'Host': 'hr.tencent.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html,"lxml")
# trs = soup.find_all('tr')[1:-1]
# trs = soup.select("tr.even")
# trs = soup.select("tr[class=even]")
# for tr in trs:
#     print(tr)
#     print("*"*30)
# alist = soup.find_all('a')
# for a in alist:
#     href = a['href']
#     print(href)
# trs = soup.find_all('tr')[1:-2]
# for tr in trs:
#     info = list(tr.stripped_strings)
#     print(info)
tables = soup.find_all('table')[0]
# for table in tables:
#     print(table)
#     print("*"*30)
print(type(tables))
# trs = tables.find_all('tr')
# for tr in trs:
#     print(tr)
# from bs4.element import Tag

