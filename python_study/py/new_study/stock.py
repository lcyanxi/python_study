#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 23:45
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : stock.py
# @Software: PyCharm
# 东方财富网股票的信息和百度股票个体信息
import requests
from bs4 import BeautifulSoup
import re
import traceback


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("获取页面出错了")


def getStcokList(lst, stcokUrl):
    html = getHtmlText(stcokUrl)
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all('a')
    for i in a:
        try:
            herf = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', herf)[0])
            print("获取股票列表完成")
        except:
            print("获取股票列表出错")
            continue


def getStcokInfo(lst, stockInfoUrl, fpath):
    for stock in lst:
        url = stockInfoUrl + stock + ".html"
        print(url)
        html = getHtmlText(url)
        try:
            if html == "":
                continue
                infoDict = {}
                soup = BeautifulSoup(html, "html.parser")
                stockinfo = soup.find('div', attrs={"class": "stock-bet"})
                name = stockinfo.find_all(attrs={"class": "bets-name"})[0]
                infoDict.update({"股票名称": name.text.split()[0]})
                keyLst = stockinfo.find_all('dt')
                valueLst = stockinfo.find_all('dd')
                for i in range(len(keyLst)):
                    key = keyLst[i].text
                    value = valueLst[i].text
                    infoDict[key] = value

                with open(fpath, 'a', encoding='utf-8') as f:
                    f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()  # 获取错误信息
            print("获取股票信息出错")


if __name__ == '__main__':
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    fpath = "D:\myStock.txt"
    infoList = []
    getStcokList(infoList, stock_list_url)
    getStcokInfo(infoList, stock_info_url, fpath)
