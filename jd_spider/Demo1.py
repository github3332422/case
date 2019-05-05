import requests, sys
url = 'http://httpbin.org/ip'
proxy = {
    'http':'60.5.254.169:8081'
}
try:
    response = requests.get(url, proxies=proxy, timeout=1)
    print(response.content.decode('utf-8'))
except requests.exceptions.ConnectionError:
    print('超时')