import requests

response = requests.get('http://47.104.173.82/neu_emotion/Home/index/showPartData.html')
print(response.text)