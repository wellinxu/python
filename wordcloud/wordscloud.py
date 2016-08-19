# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:37:40 2016

@author: Administrator
"""

from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import sys
import jieba

scode = sys.getdefaultencoding()

stopword = []
f = open(r"D:\workspace\python\flipped\stopwords.txt","r")
lines = f.readlines()
f.close()
for line in lines:
    if len(line) > 4:
        stopword.append(line.strip().decode("utf8"))

#读取文档
text = []

f = open(r"D:\workspace\python\flipped\xiyouji.txt","r")
lines = f.readlines()
f.close()
t = {}
for line in lines:
    ts = jieba.cut(line)
    for w in ts:
        if w in stopword:
            #print w
            continue
        if len(w) > 1:
            if w in t:
                t[w] = t[w] + 1
            else:
                t[w] = 1


for key in t.keys():
    text.append((key,t[key]))
#text.append(("西游记".decode("utf8"),1000))


#f = open(r"D:\workspace\python\100100000.txt","r")
#lines = f.readlines()
#for line in lines:
#    line = line.split(",")
#    if len(line) == 2 and float(line[1]) > 0.02:
#        text.append((line[0].decode("utf8"),float(line[1])))
#f.close()

#f = open(r"D:\workspace\python\flipped\flipped.txt","r")
#lines = f.readlines()
#f.close()
#s = ""
#for line in lines:
#    s = s + line
#t = {}
#ts = jieba.cut(s)
#for w in ts:
#    if w in stopword:
#        #print w
#        continue
#    if len(w) > 1:
#        if w in t:
#            t[w] = t[w] + 1
#        else:
#            t[w] = 1
#for key in t.keys():
#    text.append((key,t[key]))
#text.append(("怦然心动".decode("utf8"),1000))


#读取背景图片
text_coloring = imread(r"D:\workspace\python\flipped\dog.png")

wc = WordCloud(background_color = "white",
               #stopwords=set(stopword),
               font_path="simhei.ttf",
               mask=text_coloring,
               max_font_size=40,
               random_state=42)
             
#生成词云
wc.generate_from_frequencies(text)
#wc.fit_words(text)


#从背景图片生成颜色          
#for i in range(347):
#    for ii in range(275):
#        for iii in range(3):
##            if ii < 135 and i < 90:
##                text_coloring[i,ii,iii] = 255
#            if i < 190:
#                if text_coloring[i,ii,iii] < 5:
#                    text_coloring[i,ii,iii] = 255
##            else:
##                if text_coloring[i,ii,iii] < 50:
##                    text_coloring[i,ii,iii] = 0
##                else:
##                    text_coloring[i,ii,iii] = 255
            
image_colors = ImageColorGenerator(text_coloring)


#显示图片
plt.imshow(wc)
plt.axis("off")

plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")

plt.figure()
plt.imshow(text_coloring,cmap=plt.cm.gray)
plt.axis("off")
plt.show()


