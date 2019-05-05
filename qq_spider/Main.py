import re
import requests
from selenium import webdriver
from http import cookiejar
import pymongo
import time
import json

#掉用浏览器和MongoDB的处理
driver=webdriver.Chrome()
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['qqdb']
mycol = mydb["user"]

#模拟登陆
def login():
	#打开QQ网页
	driver.get("https://qzone.qq.com/")
	driver.switch_to_frame('login_frame')
	driver.find_element_by_id('switcher_plogin').click()
	driver.find_element_by_id('u').clear()
	driver.find_element_by_id('u').send_keys('476668643')
	driver.find_element_by_id('p').clear()
	driver.find_element_by_id('p').send_keys('zq18814664090')
	driver.find_element_by_id('login_button').click()
	time.sleep(5)
	#得把Frame的定位换回来,否则可能会出错
	driver.switch_to.default_content()
    # print(driver)
	return driver

#获取cookies的g_tk这个键的内容，并进行加密返回
def get_g_tk(cookie):
    hashes = 5381
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)  # ord()是用来返回字符的ascii码
    return hashes & 0x7fffffff

# 获取cookies,返回带cookies的requests
def back_session(driver):
    mysession = requests.session()
    cookies = driver.get_cookies()
    cookie = {}
    for elem in cookies:
        cookie[elem['name']] = elem['value']
    headers = {'host': 'h5.qzone.qq.com',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.8',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
               'connection': 'keep-alive'
               }
    c = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
    mysession.headers = headers
    mysession.cookies.update(c)
    return mysession

# 获取所有好友的QQ号,返回好友的列表
def get_allQQ(mysession, g_tk, qzonetoken):
    url_friend = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?uin='+str(476668643)+'&do=1&fupdate=1&clean=1&g_tk='+str(g_tk)+'&qzonetoken='+qzonetoken+'&g_tk='+str(g_tk)
    driver.get(url_friend)
    friendpat = '"uin":(.*?),'
    resp = driver.page_source
    # print(resp)
    friendlist = re.compile(friendpat).findall(resp)
    time.sleep(3)
    return friendlist

#获取所有好友的说说
def get_message(friend_list,mysession, qq, g_tk, qzonetoken):
    for i in range(0, len(friend_list)):
        print("现在爬取的是" + str(friend_list[i]) + "的信息")
        try:
            # get_spider(mysession, friend_list[i], g_tk, qzonetoken,i)
            print(str(friend_list[i]) + "的信息已经爬取完毕***********")
            print("\n\n")
            time.sleep(5)
        except Exception as e:
            print("该好友爬取出现问题,跳过.爬取下一位好友")
            print("\n\n")
        time.sleep(3)

# 对信息进行爬取
def get_spider(mysession, qq, g_tk, qzonetoken):
    # 这个url是存储的是好友说说的内容和时间
    url = 'https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=' + str(
        qq) + '&inCharset=utf-8&outCharset=utf-8&hostUin=' + str(
        qq) + '&notice=0&sort=0&pos=0&num=20&cgi_host=http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6&code_version=1&format=jsonp&need_private_comment=1&g_tk=' + str(
        g_tk) + '&qzonetoken=' + str(qzonetoken)
    # 内容
    cpat = '"certified".*?"conlist":(.*?),'
    # 时间
    tpat = '"certified".*?"createTime":"(.*?)"'
    # 获取总说说数,由于每个网页都会有,只爬取一次就好
    shuoshuo_number_pat = '"total":(.*?),'
    resp = mysession.get(url)
    shuoshuo_number = re.compile(shuoshuo_number_pat).findall(resp.text)[0]
    content_list = re.compile(cpat, re.S).findall(resp.text)
    # 用来检查是否可以爬取
    if len(content_list) == 0:
        print("该好友说说为0,或你被禁止查看此好友的空间")
        return False
    # 算出页数

    if int(shuoshuo_number) % 20 == 0:
        page = int(shuoshuo_number) / 20
    else:
        page = int(shuoshuo_number) / 20 + 1
    print("一共有" + str(shuoshuo_number) + "条说说")
    # 爬取接下几页的说说
    for i in range(0, int(page)):
        # 和上面的网址一样,只不过改页数需要变动pos这个参数
        pos = i * 20
        try:
            url = 'https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=' + str(
                qq) + '&inCharset=utf-8&outCharset=utf-8&hostUin=' + str(qq) + '&notice=0&sort=0&pos=' + str(
                pos) + '&num=20&cgi_host=http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6&code_version=1&format=jsonp&need_private_comment=1&g_tk=' + str(
                g_tk) + '&qzonetoken=' + qzonetoken
            resp = mysession.get(url)
            content_list = re.compile(cpat, re.S).findall(resp.text)
            time_list = re.compile(tpat, re.S).findall(resp.text)
            print("正在爬取第" + str(i + 1) + "页信息----------")
            for c, t in zip(content_list, time_list):
                try:
                    c = c.replace('[{"con":', '')
                    mydict = {
                        'time':t,
                        'date':c
                    }
                    mycol.insert_one(mydict)
                    # in_mysql(t, c,conn)
                except Exception as e:
                    print("有一条说说数据无法写入")

        except Exception as e:
            print("第" + str(i + 1) + "页信息爬取失败")

# 对好友信息就行获取
def get_allUser(mysession,friend_list, g_tk, qzonetoken):
    k = 1
    for i in friend_list:
        print('正在获取第' , k , '个人的信息')
        if k < 170:
            k += 1
            continue
        k += 1
        try:
            url = 'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/user/cgi_userinfo_get_all?uin='+str(i)+'&vuin='+str(476668643)+'&fupdate=1&g_tk='+str(g_tk)+'&qzonetoken='+str(qzonetoken)
            print(url)
            resp = mysession.get(url)
            if resp.status_code == 200:
                j = json.loads(resp.text[10:-2])
                results = j.get('data')
                if results != None:
                    mycol.insert_one(results)
                    print('插入数据成功')
                print(results,type(results))
                time.sleep(3)
        except:
            print('该好友没有任何信息')

#函数执行
def start():
    # 构造g_tk参数,这在构造网址上会有用
    driver = login()
    # 获取qzondetoken参数
    html = driver.page_source
    xpat = r'window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)'
    qzonetoken = re.compile(xpat).findall(html)[0]
    print('qzonetoken',qzonetoken)
    cookies = driver.get_cookies()
    # print('cookies',cookies)
    cookie = {}
    for elem in cookies:
        cookie[elem['name']] = elem['value']
    # print('cookie',cookie)
    g_tk = get_g_tk(cookie)
    print('g_tk',g_tk)
    mysession = back_session(driver)
    # print(mysession)
    # 接下来就可以爬取好友的信息
    friend_list = get_allQQ(mysession, g_tk, qzonetoken)
    # print('friend_list',friend_list)
    # driver.close()
    #获取所有好友
    get_allUser(mysession, friend_list, g_tk, qzonetoken)
    #获取所有的好友说说
    # get_message(friend_list, mysession, qq, g_tk, qzonetoken)

if __name__ == '__main__':
    start()