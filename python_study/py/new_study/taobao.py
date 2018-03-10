#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 22:32
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : taobao.py
# @Software: PyCharm
# 获取淘宝手机的名称和价格
import requests
import re


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取页面出错了")


def parseHtml(infoList, html):
    try:
        tpl = re.findall(r'\"title\"\:\".*?\"', html)
        ppl = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
        for var in range(len(tpl)):
            price = eval(tpl[var].split(':')[1])  #eval去除引号
            title = eval(ppl[var].split(':')[1])
            infoList.append([title, price])
    except:
        print("页面解析出错了")


def printInfo(infoList):
    tplt = "{:10}\t{:20}\t{:15}"
    print(tplt.format("序号", "手机名称", "价格"))
    count = 1
    for var in infoList:
        print(tplt.format(count, var[0], var[1]))
        count += 1


if __name__ == "__main__":
    keyword = "手机"
    start_url = "https://s.taobao.com/search?q=" + keyword
    infoList = []
    depth = 3
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48 * i)
            html = getHtmlText(start_url)
            parseHtml(infoList, html)
            printInfo(infoList)
        except:
            continue
