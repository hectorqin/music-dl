#!/usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: HJK 
@file: echo.py 
@time: 2019-01-09

控制台输出内容控制

"""
import platform

colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'pink': '\033[95m',
    'cyan': '\033[96m',

    'qq': '\033[92m',
    'kugou': '\033[94m',
    'netease': '\033[91m',
    'baidu': '\033[96m',
    'xiami': '\033[93m',
    'flac': '\033[95m',
}


def colorize(string, color):
    if not color in colors: return string
    if platform.system() == 'Windows':
        return string
    return colors[color] + string + '\033[0m'



def notice(keyword):
    print('\nSearching %s from ...' % colorize(keyword, 'yellow'), end='', flush=True)

def brand(source):
    print(' %s ...' % colorize(source.upper(), source), end='', flush=True)

def line():
    print('\n---------------------------\n')