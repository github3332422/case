import requests
from PIL import Image
from urllib import request
from http import cookiejar

cookies = {'JSESSIONID': ''}
# req = requests.session()
def get_cookies():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://172.20.139.153/validateCodeAction.do')
    for item in cookie:
        cookies['JSESSIONID'] = item.value

def get_ver(cookies):
    headers = {
        'Host': '172.20.139.153',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'image/webp,*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Cookie': cookies
    }
    response = requests.get('http://172.20.139.153/validateCodeAction.do', cookies=cookies)
    f = open('code.jpg', 'wb')
    f.write(response.content)
    f.close()

def login(cookies,ver):
    print('正在登录')
    headers = {
        'Host': '172.20.139.153',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://172.20.139.153/',
        'Connection': 'keep-alive',
        'Cookie':cookies,
        'Upgrade-Insecure-Requests': '1'
    }
    data = {
        'zjh': '2016021214',
        'mm':'07621X',
        'v_yzm':ver
    }
    url = 'http://172.20.139.153/loginAction.do'
    response = requests.post(url, cookies=cookies, data=data)
    # url = 'http://172.20.139.153/ggglAction.do?actionType=4'
    # response = requests.get(url,headers=headers)
    print(response,response.text)
    print('登录成功')

get_cookies()
print(cookies)
get_ver(cookies)
ver = input('请输入验证码')
login(cookies,ver)
