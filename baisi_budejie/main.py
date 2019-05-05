import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def parse_detil(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    users = html.xpath('//div[@class="u-txt"]')
    for user in users:
        user_name = user.xpath('./a//text()')[0]
        user_time = user.xpath('./span//text()')[0]
        print(user_name,user_time)
        print("*"*30)
    contents = html.xpath('//div[@class="j-r-list-c"]')
    print(len(contents))
    for content in contents:
        content_desc = content.xpath('./div[@class="j-r-list-c-desc"]/a/text()')[0]
        print(content_desc)
        content_img = content.xpath('./div[@class="j-r-list-c-img"]/a/img/@data-original')[0]
        print(content_img)
        print("*"*30)

def main():
    url = 'http://www.budejie.com/1'
    parse_detil(url)

if __name__ == '__main__':
    main()