#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 10:01
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : mystudy01.py
# @Software: PyCharm

from mystudy import my_test2


# 定义函数
def mystudy01(str):
    "打印任何可以传入的字符串"
    print(str)
    return "成功打印字符串"


# 调用函数
print(mystudy01("我是一名程序员"))


def myList(mylist):
    "打印数组变量"
    mylist.append([22, 33, 44, 55])
    print("内部函数结果:", mylist)
    return


mylist = [1, 2, 3, 4]
myList(mylist)
print("外置函数结果：", myList(mylist))


def mytest(*myvalue):
    "不定参数的传入"
    print("输出：", myvalue)
    for var in myvalue:
        print(var)
    return


mytest(10)
mytest(10, 20, 30, 40)

# lambda
sum = lambda arg1, arg2: arg1 + arg2
print("lambda:", sum(30, 10))

num = 2


def sum(arg1, arg2):
    "全局变量想作用于函数内，需加 global"
    global num
    num = arg2 + arg1
    print(num)
    return num


print(sum(2, 6))
print(num)

# 调用另一个模块的函数
print(my_test2.hellworld("kangkang", 24))
