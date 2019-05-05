import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

poem_links = []
def getall_urls():
    # 爬取的诗歌网址
    urls = ['https://www.gushiwen.org/gushi/tangshi.aspx','https://www.gushiwen.org/gushi/sanbai.aspx','https://www.gushiwen.org/gushi/songsan.aspx','https://www.gushiwen.org/gushi/songci.aspx']
    for url in urls:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, "lxml")
        content = soup.find_all('div', class_="sons")[0]
        links = content.find_all('a')
        for link in links:
            poem_links.append(str(link['href']))
        # print(len(poem_links),poem_links)

content_list = []
title_list = []
dynasty_list = []
poet_list = []
def get_poem(url):
    # url = 'https://so.gushiwen.org/shiwenv_45c396367f59.aspx'
    # 请求头部
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
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
    print(content,dynasty_poet,title)

def write_csv():
    df = pd.DataFrame({'title': title_list,
                       'dynasty': dynasty_list,
                       'poet': poet_list,
                       'content': content_list
                       })
    print(df.head())
    df.to_csv('./poem.csv', index=False)

def main():
    urls = getall_urls()
    print(len(poem_links),type(urls), poem_links)
    # for url in urls:
    #     print(url)
    #     get_poem(url)
    # write_csv()


if __name__ == '__main__':
    main()