import requests
import re

def parse_detail(url):
    response = requests.get(url)
    text = response.text
    authors_tab = re.findall(r'<div class="author clearfix">.*?<h2>(.*?)</h2>',text,re.DOTALL)
    authors = []
    for author in authors_tab:
        author = re.sub(r'\n',"",author)
        authors.append(author)
    print(authors)
    contents_tab = re.findall(r'<div class="content">(.*?)</div>',text,re.DOTALL)
    contents =[]
    for content in contents_tab:
        content = re.sub(r'<.*?>',"",content)
        contents.append(content.strip())
    print(contents)

def main():
    url = 'https://www.qiushibaike.com/text/page/1/'
    parse_detail(url)

if __name__ == '__main__':
    main()