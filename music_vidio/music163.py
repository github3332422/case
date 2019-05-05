import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

#music.163下载
# url = 'http://m10.music.126.net/20190505082033/809160d88e3bdb74a82630d16641ec0d/ymusic/ab12/9210/584a/b12009e573358e35cd1e44d461c2e1e8.mp3'

#qq音乐下载
url = 'http://dl.stream.qqmusic.qq.com/M500002nrXOA0ubgm5.mp3?vkey=568360736AE98EE7A85D4106D89665FC481FC3AB590945758F0CC720CCB09AA65FE88B3F98C3F41854EC253DDD2E5D90C74D78CFBB1B145C&guid=5150825362&fromtag=1'
response = requests.get(url, headers = headers)
with open("洛阳怀.mp3", "wb") as file:
    file.write(response.content)


#v.qq.com下载
# url = 'https://apd-2fe0c0589c375fe881c0f62a42de89d1.v.smtcdns.com/vhot2.qqvideo.tc.qq.com/AdXHmnpAsPIGxAAJgZNudOH1idYSR-FPwim0hnjyFJlk/uwMROfz0r5xhIaQXGdGnCmdfJ6pSirFcPw1DPTTKmzqADXz6/q0362kpx4b6.p702.1.mp4?sdtfrom=v1010&guid=f2dbbfc5b2158a20299561616dae0cee&vkey=BD002EE4FA946F8CD31978848EEF6A74409A131DA8FBF6984060161B471EC23700C19EE5D8977B1D8DA801D5C9F66C40ABFFCA0D1979958224E6C583AD4F88A0DF3250563CF04FA29F6DBC08D9B19BA04BB5B073B29EE994053B52C497472EB5B154D97A876C57391D8EA03BBB6EE431BF92BAEE642D010E'
#
# response = requests.get(url, headers = headers)
# with open("英雄儿女.mp4", "wb") as file:
#     file.write(response.content)