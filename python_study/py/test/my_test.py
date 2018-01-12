#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 16:18
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : my_test.py
# @Software: PyCharm
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 方法一
d = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (j != k) and (i != j):
                d.append([i, j, k])

print("能组成的总数：", len(d))
print(d)
# 方法二
num = [1, 2, 3, 4]
i = 0
for a in num:
    for b in num:
        for c in num:
            if (a != b) and (a != c) and (b != c):
                i += 1
                print(a, b, c)
print("总数是：", i)

# 方法三
list = []
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if x != y != z != x:
                list.append(int(str(x) + str(y) + str(z)))
print(list)
print(len(list))
