import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool
from bs4 import BeautifulSoup
import datetime
import csv

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    problem_list = []
    pattern = re.compile('<tr.*?contest">.*?<a href=".*?">.*?<a href=".*?">(.*?)</a></td>.*?title"><a href="(.*?)".*?>(.*?)</a></td>.*?result"><a href="(.*?)".*?>'
                         +'(.*?)</a></td>.*?memory">(.*?)</td>.*?spending-time">(.*?)</td>.*?code-length">(.*?)</td>'
                         +'.*?language"><a href=".*?">(.*?)</a></td>.*?date"><abbr title="(.*?)">.*?</abbr></td>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        problem_list = []
        problem_list.append(item[0])
        problem_list.append(item[1][7:10])
        problem_list.append(item[2])
        problem_list.append(item[4])
        problem_list.append(item[9])
        write_to_csv(problem_list)
    # for item in items:
    #     yield {
    #         'title': item[0],
    #         'title_url': item[1][7:10],
    #         'problem': item[2],
    #         # 'problem_url': item[3],
    #         'status': item[4],
    #         # 'memory': item[5],
    #         # 'Run_time': item[6],
    #         # 'code_length': item[7],
    #         # 'language': item[8],
    #         'time': item[9]
    #     }

def write_to_file(content):
    with open("数据.txt","a+",encoding='utf-8')as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()

def write_to_csv(list):
    with open('xzy.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list)

def main(i):
    url = 'http://openjudge.cn/user/881544/?page='+str(i)
    html = get_one_page(url)
    # for i in parse_one_page(html):
    #     write_to_file(i)
    parse_one_page(html)

if __name__ == '__main__':
    for i in range(1,22):
         main(i)


