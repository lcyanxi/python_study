#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 10:55
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : user_path_analyse_util.py
# @Software: PyCharm

import sys
import datetime

# 主要转换用户路径  截取只从首页来的  并且合并连续两个相同的路径    并且截取路径小于15步长

if __name__ == '__main__':
    # if sys.argv != 2:
    # print("===========传入的参数有问题==========")

    # 目标数据地址
    # targetPath = sys.argv[1]
    targetPath = "D:/user_path_analyse_homepage.log"
    # 生成数据地址
    # resultPath = sys.argv[2]
    resultPath = "D:/result_user_path_analyse_homepage.log"
    begin_time = datetime.datetime.now()
    tmpDict = {}
    with open(targetPath, "r", encoding="utf-8") as fr:
        for line in fr:
            userPath = line.strip().split('>')
            result = ''
            i = 0
            # 标记路径长度  15 步长
            index = 0
            isOk = False
            for target in userPath:
                # 首页>首页>首页>首页>首页>首页>首页>首页>首页>首页>首页>首页>首页>首页>首页>离开,158
                if "首页" == target and userPath[i + 1] != "首页":
                    isOk = True
                if isOk:
                    if i == len(userPath) - 1 or index == 15:
                        result += "离开"
                        isOk = False
                    # 去掉两个连续相同的路径
                    elif target != userPath[i + 1]:
                        result += target + ">"
                        index += 1
                i += 1

            if result != "" and result in tmpDict.keys():
                # 有存在的相同路径的  只把key值累加
                tmpDict[result] = int(tmpDict[result]) + 1
            elif result != "":
                tmpDict[result] = 1

    f = open(resultPath, "w")
    for tmpData in tmpDict:
        url = tmpData + "," + str(tmpDict[tmpData])
        f.writelines(url + "\n")
    f.close()
    end_time = datetime.datetime.now()
    print((end_time - begin_time).seconds)
