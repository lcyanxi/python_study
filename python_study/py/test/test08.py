#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 22:04
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : test08.py
# @Software: PyCharm
# 题目：时间函数举例3。
if __name__ == "__main__":
    import time

    startime = time.clock()
    for i in range(100000):
        print(i)
    end = time.clock()
    print(time.clock())
    print(time.time())
    print("different is %6.3f" % (end - startime))
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))
