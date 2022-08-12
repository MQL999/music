"""
#-*-coding:utf-8-*-
@Project:music
@File:urls.py
@Author:闵麒良
@Time:2022/8/9 16:08

"""

from django.urls import path
from .views import *
urlpatterns = [
    # 歌曲播放页
    path('<int:id>.html', playView, name='play'),
    # 歌曲下载
    path('download/<int:id>.html', downloadView, name='download')
]
