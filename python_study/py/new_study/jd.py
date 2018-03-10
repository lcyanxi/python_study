#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/10 11:02
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : jd.py
# @Software: PyCharm

import requests

url = "https://www.baidu.com/s"


def getHtmlText(url):
    try:
        kv = {'wd': "python"}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("爬取成功", r.request.url)
        print(r.text[0:1000])
    except:
        print("爬去失败")


if __name__ == '__main__':
    "程序的主入口"
    getHtmlText(url)
