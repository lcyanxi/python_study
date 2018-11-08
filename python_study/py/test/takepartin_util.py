#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 11:56
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : takepartin_util.py
# @Software: PyCharm
import json

if __name__ == "__main__":
    q_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    fw = open("D:/result.log", "w", encoding="utf-8")
    fw.write("用户ID>1>2>3>4>5>6>7>8>9>10>11>12>13>15>16>17>18>19>20" + "\n")
    with open("D:/tmp.log", "r", encoding="utf-8") as fr:
        for line in fr:
            data_list = line.strip().split(">")[1]
            key_list = []
            fw.write(line.strip().split(">")[0] + ">")
            for q in q_list:
                flag = True
                for word in json.loads(data_list):
                    if int(word["q"]) == q:
                        flag = False
                        fw.write(str(word["a"]).replace("'", "") + ">")
                        try:
                            fw.write(str(word["a"]).replace("'", "") + "(" + str(word["r"]) + ")>")
                        except:
                            fw.write(str(word["a"]).replace("'", "") + ">")
                if flag:
                    fw.write("0" + ">")
            fw.write("\n")
