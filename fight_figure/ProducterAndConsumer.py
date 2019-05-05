import requests
from urllib import request
from lxml import etree
import os
import re
import threading
from queue import Queue

class Producter(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producter,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        for image in images:
            image_url = image.get("data-original")
            image_name = image.get("alt")
            image_name = re.sub(r'[！，？*/?\x08。]', "", image_name)
            suffix = os.path.splitext(image_url)[1][0:-4]
            filename = image_name + suffix
            self.img_queue.put((image_url,filename))
            # # print(filename)


class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            try:
                request.urlretrieve(img_url, 'images/' + filename)
                print(filename + '  下载完成！')
            except:
                print(filename)

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        page_queue.put(url)

    for x in range(5):
        t = Producter(page_queue, img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()

if __name__ == '__main__':
    main()