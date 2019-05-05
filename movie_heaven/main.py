from lxml import etree
import requests
import time

BASE_DOMAIN = 'http://dytt8.net'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def get_detail_urls(url):
    response = requests.get(url,headers = HEADERS)
    #如果发现解码的时候有问题，但是乱码的地方对爬虫不影响的话，我们直接获取原文本就好
    # text = response.content.decode('utf-8')
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN + url,detail_urls)
    return detail_urls

def parse_info(info,rule):
    return info.replace(rule,"").strip()

def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gb2312', "ignore")
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['电影名字'] = title
    Zoom = html.xpath("//div[@id='Zoom']")[0]
    imgs = Zoom.xpath(".//img//@src")
    cover = imgs[0]
    movie['电影海报'] = cover
    if len(imgs) > 1:
        screenshot = imgs[1]
        movie['电影截图'] = screenshot
    infos = Zoom.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代　"):
            info = parse_info(info,"◎年　　代　")
            movie['上映时间'] = info
        elif info.startswith("◎产　　地　"):
            info = parse_info(info,"◎产　　地　")
            movie['电影产地'] = info
        elif info.startswith("◎类　　别　"):
            info = parse_info(info,"◎类　　别　")
            movie['电影类型'] = info
        elif info.startswith("◎豆瓣评分　"):
            info = parse_info(info,"◎豆瓣评分　")
            movie['电影评分'] = info[0:3]
        elif info.startswith("◎片　　长　"):
            info = parse_info(info,"◎片　　长　")
            movie['电影片长'] = info
        elif info.startswith("◎导　　演　"):
            info = parse_info(info,"◎导　　演　")
            movie['电影导演'] = info
        elif info.startswith("◎主　　演　"):
            starring = []
            for x in range(index, len(infos)):
                if infos[x].startswith('◎简　　介'):  # 如果到了简介，就代表主演列表结束，那么就结束循环
                    break
                starring.append(infos[x].replace('◎主　　演', '').strip())
            movie['电影主演'] = str.join('\n', starring)  # 把主演列表通过join转换成字符串
        elif info.startswith("◎简　　介 "):
            info = infos[index + 1].strip()  # 简介储存在当前下标的下一个位置
            movie['电影简介'] = info
    movie['迅雷下载'] = html.xpath("//td[@style='WORD-WRAP: break-word']//text()")[0]
    return movie

def spider():
    url = 'http://dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for i in range(1,188):
        print("获取第",i,"页的数据")
        detail_urls = get_detail_urls(url.format(i))
        for detail_url in detail_urls:
            time.sleep(1)
            print(parse_detail_page(detail_url))

if __name__ == '__main__':
    spider()



