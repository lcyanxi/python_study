#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 20:49
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : game_functions.py
# @Software: PyCharm
import sys

import pygame


def check_events(ship):
    """"响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 按下键事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        # 松开键事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """"响应按键"""
    if event.key == pygame.K_RIGHT:
        # 飞船向右移动
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    # if event.key == pygame.K_UP:
    #     ship.moving_right = True
    # if event.key == pygame.K_DOWN:
    #     ship.moving_left = True


def check_keyup_events(event, ship):
    """"响应松键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    # if event.key == pygame.K_DOWN:
    #     ship.moving_right = False
    # if event.key == pygame.K_UP:
    #     ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """"更新屏幕上的图像，并切换到屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
