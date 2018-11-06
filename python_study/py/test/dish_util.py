#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 15:12
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : dish_util.py
# @Software: PyCharm

import random
import datetime
import json


def random_util(dataList):
    # 用于存放结果的List
    resultList = []
    # 最小随机数
    min = 0
    # 最大随机数
    max = len(dataList) - 1
    COUNT = 5

    # 2、利用Python中的randomw.sample()函数实现
    # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。
    resultList = random.sample(range(min, max + 1), COUNT)

    # 打印结果
    return resultList


if __name__ == '__main__':

    dataList = []
    resultData = []
    # 读数据
    for line in open("D:\data.log"):
        dataList.append(line.strip())

    # 写数据

    for i in random_util(dataList):
        resultData.append(dataList[i].strip())

    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    f = open('D:\data_result.log', 'w')
    print(resultData)
    f.writelines(json.dumps(resultData).replace(" ","").replace('"','\\\\"') + "," + now_time + "," + now_time + "," + now_time)
    f.close()
