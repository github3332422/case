import requests
from urllib import request
from http import cookiejar

cookies = {'JSESSIONID': ''}

def get_cookies():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://172.16.50.71/')
    for item in cookie:
        cookies['JSESSIONID'] = item.value

def login():
    data = {
        'loginName':'2016021214',
        'password':'2016021214'
    }
    url = 'http://172.16.50.71/user_login.html'
    response = requests.post(url, cookies=cookies, data=data)
    # print(response, response.text)
    print('登录成功')

def get_zaochao():
    url = 'http://172.16.50.71/personQueryZC_personalDetailQuery.html'
    response = requests.get(url,cookies=cookies)
    print(response.text)

def get_tuozhan():
    url = 'http://172.16.50.71/attendanceSTTZ_list.html'
    response = requests.get(url, cookies=cookies)
    print(response.text)

def get_zizhu():
    url = 'http://172.16.50.71/attendanceZZXX_list.html'
    response = requests.get(url, cookies=cookies)
    print(response.text)

get_cookies()
print(cookies)
login()
get_zaochao()
print("*"*50)
get_tuozhan()
print("*"*50)
get_zizhu()
print("*"*50)