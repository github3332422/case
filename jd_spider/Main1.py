import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def write(lists):
    with open('ip.txt','a', encoding='utf-8') as f:
        for list in lists:
            f.writelines(list)
            f.write('\n')

def truncatefile():
    with open('ip.txt', 'w', encoding='utf-8') as f:
        f.truncate()

def read_ip():
    print('开始读入数据')
    with open("ip.txt", 'r', encoding='utf-8') as f:
        list_ip = []
        for s in f.readlines():
            list_ip.append(s.strip())
    return list_ip
    print('数据读入完成')

def check_ip(list_ip):
    real_ip = []
    for ip in list_ip:
        url = 'http://httpbin.org/ip'
        proxy = {
            'http': ip
        }
        try:
            response = requests.get(url, proxies=proxy, timeout=1,headers=headers)
            print(response.content.decode('utf-8'))
            real_ip.append(ip)
        except Exception:
            pass
            # print('超时')
    return real_ip

def get_ip(url):
    list_ip = []
    # url = 'https://www.xicidaili.com/nn/1'
    # proxy = {
    #     'http': '60.5.254.169:8081'
    # }
    text = requests.get(url,headers=headers).text
    # print(text)
    html = etree.HTML(text)
    trs = html.xpath("//tr")[1:-1]
    for tr in trs:
        # print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
        trs = tr.xpath(".//td")
        ip = trs[1]
        post = trs[2]
        ip = etree.tostring(ip, encoding='utf-8').decode('utf-8').strip()[4:-5].strip()
        post = etree.tostring(post, encoding='utf-8').decode('utf-8').strip()[4:-5].strip()
        ipaddress = ip + ":" + post
        # print(ipaddress)
        list_ip.append(ipaddress)
        # print("*"*50)
    write(list_ip)


if __name__ == '__main__':
    print('程序开始执行')
    # print('开始获取')
    # url = 'https://www.xicidaili.com/nn/{}'
    # # get_ip(url.format(1))
    # for i in range(1,2):
    #     url = url.format(i)
    #     print(url)
    #     get_ip(url)
    # print("ip获取完成")
    print('ip读入开始')
    list_ip = []
    list_ip = read_ip()
    print(len(list_ip),'ip读入完成')
    print('ip筛选开始')
    real_ip = []
    real_ip = check_ip(list_ip)
    truncatefile()
    write(real_ip)
    print('ip筛选完成')
    print('程序执行完成')