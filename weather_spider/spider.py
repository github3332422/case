import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []

def parse_page(url):
    response = requests.get(url)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_= 'conMidtab')
    # print(conMidtab)
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            tmp_td = tds[-2]
            temperature = list(tmp_td.stripped_strings)[0]
            # print({"city":city,"temperature":temperature})
            ALL_DATA.append({"city":city,"temperature":temperature})


def main():
    print('开始爬虫')
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_page(url)
    print('爬虫完成')
    #根据最低气温进行排序
    # def sort_key(data):
    #     min_temp = data['temperature']
    #     return min_temp
    print('开始排序')
    ALL_DATA.sort(key=lambda data:int(data['temperature']))
    # for i in ALL_DATA:
    #     print(i)
    print('排序完成')
    data = ALL_DATA[0:10]
    # cityes = []
    # for value in data:
    #     city = value['city']
    #     cityes.append(city)
    cityes = list(map(lambda  x:x['city'],data))
    temperature = list(map(lambda  x:x['temperature'],data))
    bar = Bar("中国天气排行榜")
    bar.add("",cityes, temperature)
    bar.render()

if __name__ == '__main__':
    main()