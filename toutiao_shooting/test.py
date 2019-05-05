import requests
import os
from multiprocessing.pool import Pool
from urllib.parse import urlencode
from hashlib import md5
import json
from bs4 import BeautifulSoup
import re


def get_page_index(offset,keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    #urlencode 把字典转化为url
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError:
        print("索引页获取失败",url)
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            # print(item.get('article_url'))
            yield item.get('article_url')

def get_page_detail(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ConnectionError:
        print("详情页获取失败",url)
        return None

def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        return result.group(1)
        # print(result.group(1))
    else:
        return None

def main():
    #获取请求页的内容
    html = get_page_index(0,'街拍')
    for url in parse_page_index(html):
        if url != None:
            html = get_page_detail(url)
            if html != None:
                result = parse_page_detail(html, url)
                print(result)
        # print('----------------------')

if __name__ == '__main__':
    main()