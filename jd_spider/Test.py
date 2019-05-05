from bs4 import BeautifulSoup
import requests
import os
url = "http://www.xicidaili.com/nn/1"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
}
r = requests.get(url=url,headers=headers)
soup = BeautifulSoup(r.text,"lxml")
server_address = soup.select(".odd > td:nth-of-type(4)")
ip_list = soup.select(".odd > td:nth-of-type(2)")
ports = soup.select(".odd > td:nth-of-type(3)")
for server,ip in zip(server_address,ip_list):
    if len(server.contents) != 1:
        print(server.a.string.ljust(8),ip.string.ljust(20), end='')
    # else:
    #     print("未知".ljust(8), ip.string.ljust(20), end='')
    # delay_time = os.popen("ping -c 1 " + ip.string + " | awk 'NR==2{print}' -")
    # delay_time = delay_time.read().split("time=")[-1].strip("")
    # print("time = " + delay_time)
