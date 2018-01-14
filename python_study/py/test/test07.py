#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 21:34
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : test07.py
# @Software: PyCharm
# 题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
# 方法一
import time
import random

if __name__ == '__main__':

    play_it = input("do you want to play it.(\'yes\'or \'no\')")
    while play_it == 'yes':
        c = input("input a character:\n")
        i = random.randint(0, 2 ** 32) % 100
        print("please input number you guess:\n")
        start = time.clock()
        a = time.time()
        guess = int(input("input your guess:\n"))
        while guess != i:
            if guess > i:
                print("please input a little smaller:\n")
                guess = int(input("input your guess:\n"))
            else:
                print("please input a little bigger:\n")
                guess = int(input("input your guess:\n"))
        end = time.clock()
        b = time.time()
        var = (end - start) / 18.2
        print(var)
        if var < 15:
            print("you are very clever")
        elif var < 25:
            print("you are normal")
        else:
            print("you are stupid")
        print("Congradulations")
        print("The number you guess is %d" % i)
        play_it = input("do you want to play it")
# 方法二

startTime = time.time()
while True:
    play = input("do you want this game(yes/no)?")
    if play == "yes":
        number = random.randint(0, 1000)
        guess = int(input("guess a number："))
        while True:
            if guess > number:
                guess = int(input("guess a smaller number:"))
            elif guess < number:
                guess = int(input("guess a bigger number:"))
            else:
                end = time.time()
                print("bingo")
                print("%0.2fs猜中" % (end - startTime))
                break

    else:
        break
