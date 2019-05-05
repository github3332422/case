import requests
from requests.exceptions import RequestException
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def get_one_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(text):
    html = etree.HTML(text)
    ul = html.xpath("//ul[@class='lists']")[0]
    # print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
    lie = ul.xpath("./li")
    for i in lie:
        # print(etree.tostring(i, encoding='utf-8').decode('utf-8'))
        title = i.xpath("@data-title")[0]
        score = i.xpath("@data-score")[0]
        release= i.xpath("@data-release")[0]
        duration = i.xpath("@data-duration")[0]
        director = i.xpath("@data-director")[0]
        actors = i.xpath("@data-actors")[0]
        picture = i.xpath(".//img/@src")[0]
        print(title,score,release,duration,director,actors,picture,sep=',')
def main():
    url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
    text = get_one_page(url)
    parse_one_page(text)


if __name__ == '__main__':
    main()