import requests
import re

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'sec_tc=AQAAAMYoTwxcJg4At8ra/D3unvWBTmEy; Hm_lvt_04660099568f561a75456483228a9516=1548661127; ASP.NET_SessionId=4gn1f1y05rwhhgbl2z0kruxc; Hm_lpvt_04660099568f561a75456483228a9516=1548661165',
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def parse_page(url):
    response = requests.get(url)
    text = response.text
    # print(text)
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    # print(titles)
    dynastys = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    # print(dynastys)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    # print(authors)
    contents_tab = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    # print(contents_tab)
    contents = []
    for content in contents_tab:
        content = re.sub(r'<.*?>', "", content)
        contents.append(content)
    poems = []
    for value in zip(titles, dynastys, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynastie': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)

def main():
    url = 'https://www.gushiwen.org/default_1.aspx'
    parse_page(url)

if __name__ == '__main__':
    main()