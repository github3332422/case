import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
# url = 'http://m10.music.126.net/20190504214914/8b62dd07fc0d5cc91cfd36438969ab05/ymusic/69e0/882f/d907/09f0056e8071111c864d4671fac35a0b.mp3'
url = 'http://dl.stream.qqmusic.qq.com/M500002nrXOA0ubgm5.mp3?vkey=A23A5C703DEE7D8D2DA77ED15FFEFC231DC9AD58F280D65EC3DA94FFCD6AEB6C578B6E2513086962CB6F98587B7C7CBEEEF6148F57410EE6&guid=5150825362&fromtag=1'

response = requests.get(url,headers=headers)
with open('hero.mp3','wb')as f:
    f.write(response.content)
