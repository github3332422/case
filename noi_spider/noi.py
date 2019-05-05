import requests
from bs4 import BeautifulSoup
import csv
from matplotlib import pyplot as plt
import datetime
import time

total_list = []
req = requests.Session()

#伪装浏览器
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Length':'58',
    'Content-Type':	'application/x-www-form-urlencoded',
    # 'Cookie':'PHPSESSID=pf95m2t6vfthhf10ri17rv6ee2',
    'Host':	'noi.openjudge.cn',
    'Pragma':'no-cache',
    'Referer':'http://noi.openjudge.cn/auth/login/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/63.0',
    'X-Requested-With':'XMLHttpRequest'
}

#用户登陆
def login(data):
    total_list.clear()
    response = req.post('http://noi.openjudge.cn/api/auth/login/', data=data)
    result = response.json()
    return result

#获取用户链接
def get_url(soup):
    return soup.findAll(name='a', attrs={'class': 'link'})[0].get('href')

#获取网页源代码
def get_html(url):
    result = req.get(url);
    result.encoding = 'utf8'
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
    return soup

#获取网页信息
def get_message(soup,name):
    message = soup.findAll('tbody')
    tab = message[0]
    headers = [c for c in soup.findAll('tr')]
    total = 0
    for i in range(2,len(headers),1):
        total += 1
        problem_list = []
        try:
            td = [c for c in headers[i].findAll('td')]
            problem_list.append(name)
            problem_list.append(td[1].string)
            problem_list.append(td[2].string)
            problem_list.append(td[6].string)
            problem_list.append(td[7].string)
            # print(problem_list)
            if total <= 30:
                write_to_csv(problem_list)
                total_list.append(problem_list)
        except:
            print('获取失败',end=" ")
    # return total_list
    time.sleep(0.4)
    print(total)
    if total == 30:
        return True
    else:
        return False

#把文件写入到csv
def write_to_csv(list):
    with open('2018.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list)

#画图
def huitu():
    Accepted = [i for i in total_list if i[2] == 'Accepted']
    WrongAnswer = [i for i in total_list if i[2] == 'Wrong Answer']
    CompileError = [i for i in total_list if i[2] == 'Compile Error']
    RuntimeError = [i for i in total_list if i[2] == 'Runtime Error']
    TimeLimitExceeded = [i for i in total_list if i[2] == 'Time Limit Exceeded']
    MemoryLimitExceeded= [i for i in total_list if i[2] == 'Memory Limit Exceeded']
    PresentationError = [i for i in total_list if i[2] == 'Presentation Error']
    data = [len(Accepted),len(WrongAnswer),len(CompileError),len(RuntimeError),len(TimeLimitExceeded),len(MemoryLimitExceeded),len(PresentationError)]
    plt.bar(range(len(data)), data)
    plt.xticks(range(len(data)), ('AC', 'WA', 'CE', 'RE', 'TLE', 'MLE', 'PE'))
    plt.show()

#执行函数
def main(user_data):
    for  user in user_data:
        print('开始信息获取',user['user_name'],'的信息')
        data = {
            'email':user['user_mail'],
            'password':user['user_password'],
            'redirectUrl':''
        }
        result = login(data)
        if result['result'] == 'SUCCESS':
            print('登陆成功')
            html = get_html('http://noi.openjudge.cn/')
            # print(html)
            url = get_url(html)
            # url = url.join('?page={}')
            print(url)
            for i in range(1, 100):
                print('正在打印', i, '页的信息', end=" ")
                url1 = url + '?page={}'.format(i)
                print(url1, end=" ")
                soup = get_html(url1)
                flg = get_message(soup,user['user_name'])
                if flg == False:
                    break
            # print(total_list)
            huitu()

        else:
            print('账号或密码错误')
            # main()

if __name__ == '__main__':
    print('开始执行')
    start_time = datetime.datetime.now()
    user_data = [
        # {'user_name':'张清','user_mail': '18814664090@qq.com', 'user_password':'zhangqing'},
        # {'user_name':'陆云凤','user_mail': '1394173753@qq.com', 'user_password': 'luyunfeng'},
        {'user_name':'王泰龙','user_mail': '1419037987@qq.com', 'user_password': '445603434'},
        {'user_name':'张磊','user_mail': '1753779123@qq.com', 'user_password': 'zhanglei9050'}
    ]
    main(user_data)
    end_time = datetime.datetime.now()
    print("总共运行时间为:%s" % (start_time - end_time))
