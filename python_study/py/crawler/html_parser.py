#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 9:49
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : html_parser.py
# @Software: PyCharm
# BeautifulSoup 安装  解压BeautifulSoup4-4.4.1.tar.gz  执行python setup.py build 和 python setup.py install
from bs4 import BeautifulSoup
import re
from  urllib import parse


class HtmlParser():
    """"page_url 基本url需要拼接部分"""

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 匹配
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))
        for link in links:
            new_url = link["href"]
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            return new_urls

    def _get_new_data(self, page_url, soup):
        red_data = {}
        red_data['url'] = page_url
        title_node =soup.find("dd",class_="lemmaWgt-lemmaTitle").find('hl')
        red_data['title']=title_node.get_text()
        summary_node=soup.find('div',class_="lemma-summary")
        red_data['summary']=summary_node.get_text()
        red_data

    #new_url 路径 html_context界面内容
    def parse(self,page_url,html_context):
        if(page_url is None or html_context is None):
            return
        # python
