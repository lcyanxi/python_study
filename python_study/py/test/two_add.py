#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 15:23
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : two_add.py
# @Software: PyCharm

import sys


class Solution(object):
    # 忘记判断32系统int表示的大小
    # 未考虑只有一位数的情况
    # 处理末尾0的时候把中间0也处理掉了901000
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = ""
        flag = True
        new_x = list(str(x))
        if x < 0:
            new_x = list(str(x).replace("-", ""))
            s = "-"
        index = len(new_x)
        if index == 1:
            return x
        for word in range(len(new_x)):
            index -= 1
            if int(new_x[index]) == 0 and flag:
                continue
            else:
                flag = False
                s += new_x[index]
        if -2 ** 31 > int(s) or int(s) > 2 ** 31 - 1:
            return 0
        return int(s)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 10000

        data_list = ["M", "D", "C", "L", "X", "V", "I"]
        print(enumerate(data_list))
        for word in range(str(s)):
            pass


if __name__ == "__main__":
    obj = Solution()
    obj.romanToInt("DMD")
