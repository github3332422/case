import requests
from lxml import etree
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection':'keep-alive',
    'Cookie': '_ga=GA1.2.1249177683.1539506743; pgv_pvi=5377200128; _gcl_au=1.1.202219451.1547373198; pgv_pvid=1246724880; PHPSESSID=7df39d47eelovnu74mupj15ld6; pgv_si=s289344512',
    'Host': 'hr.tencent.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

BASE_URL = 'https://hr.tencent.com/'

positions = []

#获取HTML页面
def get_html(url):
    '''
    获取HTML页面
    :param url:
    :return:
    '''
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    # print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
    return html

#获取一个多少页的数据
def get_total_page(html):
    '''
    获取一共有多少页的数据
    :param html:
    :return:
    '''
    total_numbers = html.xpath("//div[@class='pagenav']//a//text()")
    return total_numbers[-2]

#获取所有信息
def get_page_message(html):
    trs = html.xpath("//table[@class='tablelist']//tr")[1:-1]
    for tr in trs:
        href = tr.xpath(".//a/@href")[0]
        title = tr.xpath("./td[1]//text()")[0]
        category = tr.xpath("./td[2]//text()")[0]
        nums = tr.xpath("./td[3]//text()")[0]
        address = tr.xpath("./td[4]//text()")[0]
        pubtime = tr.xpath("./td[5]//text()")[0]
        posit = get_message_detail(BASE_URL + href)
        position = {
            '职位链接': BASE_URL + href,
            '职位名称': title,
            '职位类别': category,
            '招收人数': nums,
            '工作地点': address,
            '发出时间': pubtime,
            '其他要求':posit
        }
        print(position)
        time.sleep(0.5)
    positions.append(position)

#获取某一个职位的信息
def get_message_detail(url):
    html = get_html(url)
    trs = html.xpath("//tr[@class='c']/td/ul")
    duties = trs[0].xpath("./li//text()")
    claim = trs[1].xpath("./li//text()")
    posit ={
        'duties':duties,
        'claim':claim
    }
    return posit

def main():
    frist_url = 'https://hr.tencent.com/position.php?keywords=Python&lid=0&tid=0&start=0'
    html = get_html(frist_url)
    total = get_total_page(html)
    for i in range(0, int(total)):
        print("正在获取第", i + 1, "页的数据")
        url = 'https://hr.tencent.com/position.php?keywords=Python&lid=0&tid=0&start={}'.format(i * 10)
        html = get_html(url)
        get_page_message(html)
        time.sleep(1)

if __name__ == '__main__':
    main()