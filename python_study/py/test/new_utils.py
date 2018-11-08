#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 17:43
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : new_utils.py
# @Software: PyCharm

import json

if __name__ == "__main__":
    q_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    one1_dict = {}
    one2_dict = {}
    one3_dict = {}
    one4_dict = {}
    one5_dict = {}
    one6_dict = {}
    one7_dict = {}
    one8_dict = {}
    one9_dict = {}
    one10_dict = {}
    one11_dict = {}
    one12_dict = {}
    one13_dict = {}
    one14_dict = {}
    one15_dict = {}
    one16_dict = {}
    one17_dict = {}
    one18_dict = {}
    one19_dict = {}


    def util(words, data_dict):
        for word in words.replace(" ", "").split(","):
            if int(word) in data_dict.keys():
                data_dict[int(word)] = int(data_dict[int(word)]) + 1
            else:
                data_dict[int(word)] = 1
        return sorted(data_dict.items(), key=lambda x: x[0])


    def str_replace(x):
        return x.replace("{", "").replace("}", "").replace("'", "").replace(":", ",")


    fw = open("D:/my_data.log", "w", encoding="utf-8")
    with open("D:/result.log", "r", encoding="utf-8") as fr:
        for line in fr:
            data_list = line.strip().replace("[", "").replace("]", "").split(">")
            util(data_list[0], one1_dict)
            util(data_list[1], one2_dict)
            util(data_list[2], one3_dict)
            util(data_list[3], one4_dict)
            util(data_list[4], one5_dict)
            util(data_list[5], one6_dict)
            util(data_list[6], one7_dict)
            util(data_list[7], one8_dict)
            util(data_list[8], one9_dict)
            util(data_list[9], one10_dict)
            util(data_list[10], one11_dict)
            util(data_list[11], one12_dict)
            util(data_list[12], one13_dict)
            util(data_list[13], one14_dict)
            util(data_list[14], one15_dict)
            util(data_list[15], one16_dict)
            util(data_list[16], one17_dict)
            util(data_list[17], one18_dict)
            util(data_list[18], one19_dict)

    fw.write(str_replace(str(one1_dict)) + "\n")
    fw.write(str_replace(str(one2_dict)) + "\n")
    fw.write(str_replace(str(one3_dict)) + "\n")
    fw.write(str_replace(str(one4_dict)) + "\n")
    fw.write(str_replace(str(one5_dict)) + "\n")
    fw.write(str_replace(str(one6_dict)) + "\n")
    fw.write(str_replace(str(one7_dict)) + "\n")
    fw.write(str_replace(str(one8_dict)) + "\n")
    fw.write(str_replace(str(one9_dict)) + "\n")
    fw.write(str_replace(str(one10_dict)) + "\n")
    fw.write(str_replace(str(one11_dict)) + "\n")
    fw.write(str_replace(str(one12_dict)) + "\n")
    fw.write(str_replace(str(one13_dict)) + "\n")
    fw.write(str_replace(str(one14_dict)) + "\n")
    fw.write(str_replace(str(one15_dict)) + "\n")
    fw.write(str_replace(str(one16_dict)) + "\n")
    fw.write(str_replace(str(one17_dict)) + "\n")
    fw.write(str_replace(str(one18_dict)) + "\n")
    fw.write(str_replace(str(one19_dict)) + "\n")
    fw.close()
