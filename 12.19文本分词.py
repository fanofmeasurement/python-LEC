# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:29:02 2018

@author: haoyu
"""

##访谈词云
import numpy as np 
import pandas as pd
import jieba
#读取文件
path = r'D:\软件\微信\文件\WeChat Files\liuhaoyun123456\Files\Master\本科python\\'
data = pd.read_excel(path+'访谈.xlsx')
ys = ''.join(data.iloc[:,0].values.tolist())
ls = ''.join(data.iloc[:,1].values.tolist())
zw = ''.join(data.iloc[:,2].values.tolist())

ys_cut = jieba.lcut(ys)#优势
ls_cut = jieba.lcut(ls)#劣势
zw_cut = jieba.lcut(zw)#展望

#停用词处理
sw = open(path+'stopword.txt','r',encoding='utf-8').read()
for i,j,k in zip(ys_cut, ls_cut, zw_cut):
    if i in sw:
        ys_cut.remove(i)
    if j in sw:
        ls_cut.remove(j)
    if k in sw:
        zw_cut.remove(k)



###开始绘制
import matplotlib as mpl
import matplotlib.pyplot as plt
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.size'] = 10

from wordcloud import WordCloud,STOPWORDS

backgroud_Image = plt.imread(path + '词云\\词云1.jpg')
wc = WordCloud(font_path='simhei.ttf', stopwords=STOPWORDS, background_color='white', max_words=1000, mask=backgroud_Image)
wc.generate(' '.join(ys_cut))
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\ys.png', dpi=1000)
plt.show()

backgroud_Image = plt.imread(path + '词云\\词云5.jpg')
wc = WordCloud(font_path='simhei.ttf', stopwords=STOPWORDS, background_color='white', max_words=1000, mask=backgroud_Image)
wc.generate(' '.join(ls_cut))
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\ls.png', dpi=1000)
plt.show()

backgroud_Image = plt.imread(path + '词云\\词云3.jpg')
wc = WordCloud(font_path='simhei.ttf', stopwords=STOPWORDS, background_color='white', max_words=1000, mask=backgroud_Image)
wc.generate(' '.join(zw_cut))
plt.imshow(wc)
plt.axis("off")
plt.savefig(path+'词云\\zw.png', dpi=1000)
plt.show()