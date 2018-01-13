#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 19:16
# @Author  : lcyanxi
# @Email    : lcyanxi@163.com
# @File    : settings.py
# @Software: PyCharm
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
