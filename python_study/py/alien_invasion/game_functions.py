#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 20:49
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : game_functions.py
# @Software: PyCharm
import sys

import pygame


def check_events():
    """"响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """"更新屏幕上的图像，并切换到屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
