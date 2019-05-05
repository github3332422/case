from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba


# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result


with open("data1.txt",encoding='utf8') as fp:
    text = fp.read()
    # print(text)
    # 将读取的中文文档进行分词
    text = trans_CN(text)
    mask = np.array(image.open("D:\picture\cy.jpg"))
    wordcloud = WordCloud(
        # background_color='white',
        # 添加遮罩层
        mask=mask,
        # 生成中文字的字体,必须要加,不然看不到中文
        font_path="C:\Windows\Fonts\STXINGKA.TTF"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
    wordcloud.to_file("2652842878.jpg")