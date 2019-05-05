# python3.6环境
from urllib import request
from http import cookiejar
from selenium import webdriver

driver = webdriver.Chrome()
if __name__ == '__main__':
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    # response = opener.open('http://172.20.139.153/validateCodeAction.do')
    response = driver.get('https://www.lagou.com/jobs/list_?labelWords=&fromSearch=true&suginput=')
    print(response)
    # 打印cookie信息
    for item in cookie:
        print(item.name,'=',item.value)
