#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 20:49
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : game_functions.py
# @Software: PyCharm
import sys

import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """"响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 按下键事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 松开键事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
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
    if event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)


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


def update_screen(ai_settings, screen, ship, bullets):
    """"更新屏幕上的图像，并切换到屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullents(bullets):
    """更新子弹位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """"如果还没有达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
