import requests

url = 'https://y.qq.com/n/yqq/song/002nrXOA0ubgm5.html'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

response = requests.get(url,headers=header)
print(response.text)