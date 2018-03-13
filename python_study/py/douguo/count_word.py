#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 13:54
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : count_word.py
# @Software: PyCharm
import string


# 题目： 输入一行字符，分布统计出其中的英文字符、空格、数字、和其他字符
def count_word():
    str = input("请输入一行字符串：")
    english_word = 0
    space_word = 0
    digit_wod = 0
    other = 0
    for var in str:
        if var.isalpha():
            english_word += 1
        elif var.isdigit():
            digit_wod += 1
        elif var.isspace():
            space_word += 1
        else:
            other += 1
    print("english_word:", english_word, "space_word:", space_word, "digit_word:", digit_wod, "other:", other)
    return


def Zodiac(month, day):
    n = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
    d = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
    return n[len(filter(lambda y: y <= (month, day), d)) % 12]


# 函数执行入口
if __name__ == '__main__':
    count_word()
    Zodiac(3, 14)
