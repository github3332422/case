from lxml import etree

file = open('2.txt','r',encoding='UTF-8')
text = file.read()
# print(text)
response = etree.HTML(text)

# tdd = response.xpath("//table[@class='titleTop2']")[0]
# tdd = tdd.xpath(".//thead")[0]
# trs = tdd.xpath(".//tr")
# # print(trs)
# print(len(trs))
trs = response.xpath("//tr[@class='odd']")
print(len(trs))
for tr in trs:
    # print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
    # print(tr)
    tds = tr.xpath(".//td//text()")
    print("*" * 50)
    for td in tds:
        print(td.strip(), end=' ')
    print()