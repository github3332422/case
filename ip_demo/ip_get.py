'''
获取当前的IP地址
'''
import requests
import re
from requests.exceptions import RequestException

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def get_ip(html):
    pattern = re.compile('"origin": "(.*?)"')
    item = re.findall(pattern, html)
    return item[0]

def main():
    url = 'http://httpbin.org/ip'
    html = get_html(url)
    ip = get_ip(html)
    print(ip)

if __name__ == '__main__':
    main()

