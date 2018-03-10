#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 17:29
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : univ_sort.py
# @Software: PyCharm
# 中国大学排名
import requests
from bs4 import BeautifulSoup
import bs4


def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


def fillUnivList(univList, html):
    soup = BeautifulSoup(html, "html.parser")
    i = 1
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            univList.append([i, tds[1].string, tds[2].string, tds[3].string])
            i += 1


def printUnivList(univList, num):
    tplt = "{0:^10}\t{1:{4}^15}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名", "学校名称", "城市", "分数", chr(12288)))  # chr(12288)中文排版对齐
    for i in range(num):
        u = univList[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))


if __name__ == "__main__":
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    univList = []
    html = getHtmlText(url)
    fillUnivList(univList, html)
    printUnivList(univList, 100)
