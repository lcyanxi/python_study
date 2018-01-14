#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 18:25
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : test04.py
# @Software: PyCharm
# 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# python 3已经没有raw_input方法了
# 方法一
if __name__ == '__main__':
    from sys import stdout

    filename = input("请输入文件名：\n")
    fp = open(filename, 'w')
    ch = input("输入字符串：\n")
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()
# 方法二
filename = input("请输入文件名：\n")
fp = open(filename, 'w+')
ch = ""
while '#' not in ch:
    fp.write(ch)
    ch = input("输入字符串：\n")
fp.close()
