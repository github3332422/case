import requests
from bs4 import BeautifulSoup

cookies = {'JSESSIONID': ''}
def getVerimg():
    url = 'http://172.20.139.153/validateCodeAction.do'
    img_data = requests.get(url)
    cookies['JSESSIONID'] = img_data.cookies['JSESSIONID']
    # print(img_data.cookies)
    # print(img_data.headers['Set-Cookie'])
    # cookies = img_data.headers['Set-Cookie'].split(';')[0]
    # print(cookies)
    f = open('ver.jpg','wb')
    f.write(img_data.content)
    f.close()

def login(ver_code):
    url = 'http://172.20.139.153/loginAction.do'
    post_data = {
        'zjh': '2016021214',
        'mm': '07621X',
        'v_yzm': ver_code
    }
    post_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '82',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies,
        'Referer': 'http://172.20.139.153/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    login_data = requests.post(url=url,data=post_data,cookies=cookies)
    print(login_data.text)
    soup = BeautifulSoup(login_data.text, 'html.parser')
    print(soup.title,type(soup.title),type(str(soup.title)))
    # print('<title>学分制综合教务</title>  ')
    if str(soup.title) == '<title>学分制综合教务</title>':
        return True
    else:
        return False

def get_kebiao():
    url = 'http://172.20.139.153/xkAction.do?actionType=6'
    post_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '82',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies,
        'Referer': 'http://172.20.139.153/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    login_data = requests.get(url=url, cookies=cookies)
    print(login_data.text)

def get_score():
    url = 'http://172.20.139.153/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001'
    post_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '82',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies,
        'Referer': 'http://172.20.139.153/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    login_data = requests.get(url=url, cookies=cookies)
    print(login_data.text)
def main():
    getVerimg()
    ver_code = input('输入验证码：')
    return ver_code

if __name__ == '__main__':
    ver_code = main()
    flg = login(ver_code)
    print(flg)
    if flg:
        get_score()
    else:
        print('验证码输入错误')
