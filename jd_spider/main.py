import requests
from bs4 import BeautifulSoup
import xlwt

def pachong(url,c):
    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text,"lxml")
    html = soup.select(".date > tr > td")
    for i in range(25):
        worksheet.write(i+25*c, 0, label = html[0+7*i].text)
        worksheet.write(i+25*c, 1, label = html[1+7*i].text)
        worksheet.write(i+25*c, 2, label = html[2+7*i].text)
        worksheet.write(i+25*c, 3, label = html[3+7*i].text)
        worksheet.write(i+25*c, 4, label = html[4+7*i].text)
        worksheet.write(i+25*c, 5, label = html[5+7*i].text)
        worksheet.write(i+25*c, 6, label = html[6+7*i].text)



if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(10):
        lianjie = "http://www.cbooo.cn/year?year="+str(2009+i)
        pachong(lianjie,i)
    workbook.save('Excel_Workbook.xls')