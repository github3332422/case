# import requests
# from PIL import Image
#
#
# headers = {
#     'Host': '172.20.139.153',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
#     'Accept': 'image/webp,*/*',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Accept-Encoding': 'gzip, deflate',
#     'Connection': 'keep-alive',
#     'Cookie': 'JSESSIONID=bahLPZDYT7qqwbR5kcjPw'
# }
# response = requests.get('http://172.20.139.153/validateCodeAction.do',headers=headers)
# print('正在保存验证码图片')
# codeImage = response.content
# fn = open('code.png','wb')
# fn.write(codeImage)
# fn.close()
# print('验证码图片保存完成')
#
# img=Image.open('code.png')
# img.show()

print('<title>学分制综合教务</title>' == '<title>学分制综合教务</title>')