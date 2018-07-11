#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 11:02
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : jd.py
# @Software: PyCharm

import requests
import sys
from time import sleep
from bs4 import BeautifulSoup
import bs4

url = "https://www.baidu.com/s"


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def viewBar(i):
    """
    进度条效果
    :param i:
    :return:
    """
    output = sys.stdout
    for count in range(0, i + 1):
        second = 0.1
        sleep(second)
        output.write('\rcomplete percent:%.0f%%' % count)
    output.flush()


def findFoodDetailList(html):
    soup = BeautifulSoup(html, "html.parser")
    # 查看网页源代码后发现 排名信息 在tbody标签 中的 tr标签
    food_name = soup.find('h1', 'color-yellow').get_text()
    food_nickname = ""
    try:
        nicknames = soup.find('h2', 'h3 text-light').get_text()
        food_nickname = nicknames.split('：')[1]
    except:
        print('qqqqqqqqqqqqq')
        food_nickname = "无"

    tables = soup.find_all('table', 'table table-hover')
    infolist = []
    dic = {}
    for table in tables:
        for tr in table.find_all('tr'):
            trs = tr.find_all('td')
            if len(trs) == 3:
                info = {}
                info[trs[0].get_text()] = trs[1].get_text() + trs[2].get_text()
                infolist.append(info)
    dic['name'] = food_name
    dic['nickname'] = food_nickname
    dic['info'] = infolist
    print(dic)


if __name__ == '__main__':
    "程序的主入口"
    starturl = "http://www.foodwake.com/food/235"
    html= getHtmlText(starturl)
    findFoodDetailList(html)
