#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 15:34
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : getjpg.py
# @Software: PyCharm
# 获取整个页面数据
import urllib.request
import re


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImage(html):
    reg = r'src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    # python3需要
    html = html.decode('utf-8')
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1


html = getHtml("http://news.china.com/internationalgd/10000166/20180115/31957609.html")

print(getImage(html))
