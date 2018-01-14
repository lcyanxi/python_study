#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 18:56
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : test06.py
# @Software: PyCharm
# 题目：字符串日期转换为易读的日期格式。
# 安装源码包 pip install python-dateutil
import time
from dateutil import parser

# 获取当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
print(parser.parse("Aug 28 2015 12:00AM"))
