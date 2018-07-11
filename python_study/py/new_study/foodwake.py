#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 17:24
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : foodwake.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # 查看网页源代码后发现 排名信息 在tbody标签 中的 tr标签
    divs = soup.find_all('div', 'row margin-b2')
    for div in divs:
        tag_as = div.find_all('a')
        for tag in tag_as:
            tag_hef = tag.get('href')
            ulist.append(tag_hef)
    return ulist


def findChildList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # 查看网页源代码后发现 排名信息 在tbody标签 中的 tr标签
    divs = soup.find_all('div', 'row margin-b2')
    for div in divs:
        tag_as = div.find_all('a')
        for tag in tag_as:
            tag_hef = tag.get('href')
            ulist.append(tag_hef)
    return ulist


def findFoodDetailList(html, fpath):
    soup = BeautifulSoup(html, "html.parser")
    # 查看网页源代码后发现 排名信息 在tbody标签 中的 tr标签
    food_name = soup.find('h1', 'color-yellow').get_text()
    food_nickname = ""
    try:
        nicknames = soup.find('h2', 'h3 text-light').get_text()
        food_nickname = nicknames.split('：')[1]
    except:
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
    with open(fpath, 'a', encoding='utf-8') as f:
        f.write(str(dic) + '\n')


def main():
    uinfo = []
    url = 'http://www.foodwake.com/category/food-class/0'
    fpath = "D:\data.txt"
    html = getHTMLText(url)
    food_class = fillUnivList(uinfo, html)
    food = []
    for i in range(len(food_class)):
        html = getHTMLText(food_class[i])
        findChildList(food, html)
        print('正在初始化数据。。。。。。。。。。。。。。。。')

    total=len(food)
    print('解析数据开始。。。。。。。。。。。。。。。。')
    for j in range(total):
        try:
            html = getHTMLText(food[j])
            findFoodDetailList(html, fpath)
            print('正在查询详细信息，请稍等。。。。。。。。。。。。。'+str(total-j))
        except:
            print("************"+food[j]+"链接解析异常")

main()
