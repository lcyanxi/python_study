#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 17:27
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : test01.py
# @Software: PyCharm
# 题目：列表转换为字典。
# 方法一
name = ['kangkang', 'lihua', 'xiaoming', 'mali']
record = [78, 98, 79, 60]
print(dict(zip(name, record)))

# 方法二
keys = ['kangkang', 'lihua', 'xiaoming', 'mali']
values = [78, 98, 79, 60]
print({keys[i]: values[i] for i in range(len(keys))})

# 方法三 python自带函数setdefault

dstList = {}
for i in range(len(keys)):
    dstList.setdefault(keys[i], values[i])
print(dstList)
