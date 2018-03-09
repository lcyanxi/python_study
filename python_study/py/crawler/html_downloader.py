#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 23:11
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : html_downloader.py
# @Software: PyCharm
from urllib import request
from urllib.parse import quote
import string


class Html_downloader():
    """"下载页面类容"""

    def download(self, new_url):
        if (new_url is None):
            return None
        # 解决请求路径中有中文或者特殊字符
        url_ = quote(new_url, safe=string.printtable)
        response = request.urlopen(url_)
        if (response.getcode() != 200):
            return None
        html = response.read()
        return html.decode("utf8")
