#--utf8--
import requests

def get_message(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError:
        print("索引页获取失败",url)
        return None

def analysis_message():
    pass

def main():
    url = 'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/user/cgi_userinfo_get_all?uin=1394173753&vuin=2652842878&fupdate=1&g_tk=128245010&qzonetoken=a6f559e3782d47341fa419655c7355aa50a4d974e550dcd0c8348d70127acaeb935fa9b4dce220454ccf46'
    html = get_message(url)
    print(html)

if __name__ == '__main__':
    main()