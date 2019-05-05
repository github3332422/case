from lxml import etree

file = open('1.txt','r',encoding='UTF-8')
text = file.read()
response = etree.HTML(text)

tdd = response.xpath("//td[@class='pageAlign']")[1]
trs = tdd.xpath(".//tr")
for tr in trs:
    # print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
    tds = tr.xpath(".//td//text()")
    for td in tds:
        print(td.strip(),end=' ')
    # print(tr)
    print("*"*100)