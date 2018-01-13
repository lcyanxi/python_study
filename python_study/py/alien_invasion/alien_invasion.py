#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 18:54
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : alien_invasion.py
# @Software: PyCharm
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    while True:
        # 响应鼠标事件
        gf.check_events(ship)
        ship.update()
        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
# 初始化游戏并创建一个屏幕对象
