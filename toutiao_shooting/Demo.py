from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from hashlib import md5
from multiprocessing import Pool
from config import *
import pymongo
import requests
import json
import re
import os

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def get_page_index(offset, keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    data = {'format': 'json', 'offset': offset, 'keyword': keyword, 'autoload': 'true', 'count': 20, 'cur_tab': 1,
            'from': 'search_tab', 'pd': 'synthesis'}
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页失败',url)
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页页失败',url)
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: JSON.parse\((.*?)\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        print(result.group(1))
        # data = json.loads(result.group(1))
        # data = json.loads(data)  # 将字符串转为dict，因为报错了
        # if data and 'sub_images' in data.keys():
        #     sub_images = data.get('sub_images')
        #     images = [item.get('url') for item in sub_images]
        #     for image in images: download_image(image)
        #     return {
        #         'title': title,
        #         'images': images,
        #         'url': url
        #     }


def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongoDb成功', result)
        return True
    return False


def download_image(url):
    print('正在下载', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.    36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片失败', url)
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)


def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            parse_page_detail(html, url)
            # result = parse_page_detail(html, url)
            # if isinstance(result, dict):
            #     save_to_mongo(result)


if __name__ == '__main__':
    # groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    # pool = Pool()
    # pool.map(main, groups)
    main(0)