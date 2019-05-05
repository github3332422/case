from urllib import request
from http import cookiejar

import requests

cookies = {'ASPSESSIONIDSCACRTDR': ''}

def get_cookies():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://172.16.50.93/')
    for item in cookie:
        cookies['ASPSESSIONIDSCACRTDR'] = item.value

def login():
    data = {
        'student':'2017024105',
        'password':'120013'
    }
    url = 'http://172.16.50.93/xk/index.asp'
    response = requests.post(url, cookies=cookies, data=data)
    # print(response, response.text)
    print('登录成功')
    print(requests.get('http://172.16.50.93/xk/index.asp',cookies=cookies).text)

def dati():
    pass

get_cookies()
print(cookies)
login(cookies)
