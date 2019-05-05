import requests
from urllib import request
from lxml import etree
import os
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def parse_page(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    print(len(images))
    for image in images:
        image_url = image.get("data-original")
        image_name = image.get("alt")
        image_name = re.sub(r'[！，？*]',"",image_name)
        suffix = os.path.splitext(image_url)[1][0:-4]
        filename = image_name + suffix
        # print(filename)
        request.urlretrieve(image_url,'images/'+filename)


def main():
    for i in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page={}'.format(i)
        print('正在打印第',i,'页的数据')
        parse_page(url)

if __name__ == '__main__':
    main()