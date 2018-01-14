#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 13:41
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """"一个对飞船发射子弹进行管理的类"""

    def __init__(self, ai_settins, screen, ship):
        """"在飞船所在的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）出创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settins.bullet_width, ai_settins.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示的子弹位置
        self.y = format(self.rect.y)

        self.color = ai_settins.bullet_color
        self.speed_factor = ai_settins.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """"在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
