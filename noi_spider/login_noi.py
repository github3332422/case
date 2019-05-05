import requests
from bs4 import BeautifulSoup
req = requests.Session()
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'58',
    'Content-Type':	'application/x-www-form-urlencoded',
    'Cookie':'PHPSESSID=pf95m2t6vfthhf10ri17rv6ee2',
    'Host':	'noi.openjudge.cn',
    'Pragma':'no-cache',
    'Referer':'http://noi.openjudge.cn/auth/login/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/63.0',
    'X-Requested-With':'XMLHttpRequest'
}
data = {
    'email':'1394173753@qq.com',
    'password':'luyunfeng',
    'redirectUrl':''
}
response = req.post('http://noi.openjudge.cn/api/auth/login/',data = data)
result = response.json()
print(result)
res = req.get(url='http://noi.openjudge.cn/')
res.encoding = 'utf8'
# print(res.text)

soup = BeautifulSoup(res.text,'html.parser')
# print(soup)
# print(soup.findAll(name='a',attrs={'class':'link'})[0].get('href'))
print(soup)