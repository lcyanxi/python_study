#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 22:55
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : url_manager.py
# @Software: PyCharm
class urlManager():
    """"URL管理类"""

    # 构造函数初始化set集合
    def __init__(self):
        self.new_urls = set()  # 待爬取得url
        self.old_urls = set()  # 已经爬取得url

    # 向管理器添加一个新的url
    def add_new_url(self, root_url):
        if (root_url is None):
            return
        if (root_url not in self.new_urls and root_url not in self.old_urls):
            self.new_urls.add(root_url)

    # 向管理器批量添加url
    def add_new_urls(self, root_urls):
        if (root_urls is None or len(root_urls) == 0):
            return
        for url in root_urls:
            self.add_new_url(url)

    # 判断是否有新的待爬取得url
    def has_new_url(self):
        return self.new_urls != 0

    # 获取一个待爬取得url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
