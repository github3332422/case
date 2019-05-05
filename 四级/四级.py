#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2018/8/24 9:37
# @Author: wardseptember
# @File: CountHighFrequencyWords.py
import re

excludes = ['the', 'of', 'to', 'and', 'in', 'a', 'is', 'were', 'was', 'you',
            'I', 'he', 'his', 'there', 'those', 'she', 'her', 'their',
            'that', '[a]', '[b]', '[c]', '[d]', 'them', 'or','for','as',
            'are','on','it','be','with','by','have','from','not','they',
            'more','but','an','at','we','has','can','this','your','which','will',
            'one','should','points)','________','________.','all','than','what',
            'people','if','been','its','new','our','would','part','may','some','i',
            'who','answer','when','most','so','section','no','into','do','only',
            'each','other','following','had','such','much','out','--','up','these',
            'even','how','directions:','use','because','(10','time','(15','[d].',
            '-','it.','[b],','[a],','however,','1','c','1.','2.','b','d','a','(10',
            '2','12.','13.','29.','3.','4.','5.','6.','7.','8.','9.','10.','11.','14.',
            '15.']
#自行过滤简单词，太多了不写了
def getTxt():
    txt = open('86_17_1_2.txt').read()
    txt = txt.lower()
    for ch in '!"@#$%^&*()+,-./:;<=>?@[]_`~{|}': #替换特殊字符
        txt.replace(ch, ' ')
    return txt
#1.获取单词
EngTxt = getTxt()

#2.切割为列表格式
txtArr = EngTxt.split()

#3.遍历统计
counts = {}
for word in txtArr:
    flag=True
    for word1 in excludes:
        if word==word1:
            flag=False
        else:
            continue
    if flag is True:
        counts[word] = counts.get(word, 0) + 1
    else:
        continue

#4.转换格式，方便打印，将字典转换为列表
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True)#按次数从大到小排序

#5.打印输出
for word,count in countsList:
    with open('output_3.txt','a+') as f:
        str1=word+' : '+str(count)+ '次'
        f.writelines(str1+'\n')
        f.close()
    #print('{0:<10}{1:>5}'.format(word,count))