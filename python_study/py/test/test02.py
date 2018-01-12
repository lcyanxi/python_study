#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 18:06
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : test02.py
# @Software: PyCharm
# 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

# read()          一次性读取文本中全部的内容，以字符串的形式返回结果
# readline()      只读取文本第一行的内容，以字符串的形式返回结果
# readlines()     读取文本所有内容，并且以数列的格式返回结果，一般配合for in使用
# 方法一
if __name__ == '__main__':
    import string

    fp = open('D:/text1.txt')
    a = fp.read()
    fp.close()

    fp = open('D:/text2.txt')
    b = fp.read()
    fp.close()

    fp = open('D:/text3.txt', 'w')
    dst = list(a + b)
    dst.sort()
    s = ''
    s = s.join(dst)
    fp.write(s)
    fp.close()

# join 相当于字符拼接符
# 方法二
with open('D:/text1.txt')as f1, open('D:/text2.txt') as f2, open('D:/text3.txt', 'w') as f3:
    for a in f1:
        b = f2.read()
    c = list(a + b)
    c.sort()
    d = ''
    d = d.join(c)
    f3.write(d)


# 方法三
def myRead(filename):
    f = open(filename, 'r+')
    target = f.readlines()
    return target


s = list("".join(myRead("D:/text1.txt") + myRead("D:/text2.txt")))
s.sort()
s1 = " ".join(s)
t = open("D:/text4.txt", "w+")
t.writelines(s1)
t.close()
