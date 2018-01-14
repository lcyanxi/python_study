#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 18:11
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : test03.py
# @Software: PyCharm
# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
import sys

if __name__ == '__main__':
    fp = open('test03.txt', 'w')
    string = input('please input a string :\n')
    string = string.upper()
    fp.write(string)
    fp = open('test03.txt', 'r')
    print(fp.read())
    fp.close()

# 方法二
str = input("请输入一个字符串：\n")
with open('test03.txt', 'w') as fp:
    fp.write(str.upper())
    print(str.upper())
    fp.close()
