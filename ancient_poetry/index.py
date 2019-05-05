import re
from lxml import etree
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

poem_list = []
def getall_urls():
    poem_list = []
    # urls = ['https://www.gushiwen.org/gushi/tangshi.aspx', 'https://www.gushiwen.org/gushi/sanbai.aspx',
    #         'https://www.gushiwen.org/gushi/songsan.aspx', 'https://www.gushiwen.org/gushi/songci.aspx']
    # urls = ['https://so.gushiwen.org/gushi/shijiu.aspx','https://so.gushiwen.org/gushi/shijing.aspx',
    #         'https://so.gushiwen.org/gushi/chuci.aspx','https://so.gushiwen.org/gushi/yuefu.aspx']
    urls = ['https://so.gushiwen.org/gushi/shijiu.aspx']
    for url in urls:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        text = requests.get(url, headers=headers)
        html = etree.HTML(text.text)
        typeconts = html.xpath("//div[@class='typecont']")
        for typecont in typeconts:
            poems = typecont.xpath(".//span/a/@href")
            for poem in poems:
                poem = "https://so.gushiwen.org" + poem
                poem_list.append(poem)
    print(len(poem_list),type(poem_list),poem_list)
    return poem_list

content_list = []
title_list = []
dynasty_list = []
poet_list = []
url_list = []
def get_poem(url):
    url_list.append(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    poem = soup.find('div', class_='contson').text.strip()
    poem = poem.replace(' ', '')
    poem = re.sub(re.compile(r"\([\s\S]*?\)"), '', poem)
    poem = re.sub(re.compile(r"（[\s\S]*?）"), '', poem)
    poem = re.sub(re.compile(r"。\([\s\S]*?）"), '', poem)
    poem = poem.replace('!', '！').replace('?', '？').replace('\n', '')
    content = poem
    if content:
        content_list.append(content)
    else:
        content_list.append('')
    # 诗歌朝代，诗人
    dynasty_poet = soup.find('p', class_='source').text
    if '：' in dynasty_poet:
        dynasty, poet = dynasty_poet.split('：')
    else:
        dynasty, poet = '', ''

    dynasty_list.append(dynasty)
    poet_list.append(poet)

    # 诗歌标题
    title = soup.find('h1').text
    if title:
        title_list.append(title)
    else:
        title_list.append('')
    print(content, dynasty_poet, title)

def write_csv():
    df = pd.DataFrame({'title': title_list,
                       'dynasty': dynasty_list,
                       'poet': poet_list,
                       'content': content_list,
                       'url': url_list
                       })
    print(df.head())
    df.to_csv('./poem.csv', index=False)

def main():
    urls = getall_urls()
    print(len(poem_list),len(content_list))
    for url in urls:
        print(url)
        get_poem(url)
        time.sleep(1)
    print(len(poem_list), len(content_list))
    write_csv()


if __name__ == '__main__':
    main()