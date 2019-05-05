import requests

req = requests.Session()
headers ={
    'Host': '172.20.139.153',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://172.20.139.153/',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=bahLPZDYT7qqwbR5kcjPw',
    'Upgrade-Insecure-Requests': '1'
}
data = {

}
response = req.get('http://172.20.139.153/',headers=headers)
print(response.text)