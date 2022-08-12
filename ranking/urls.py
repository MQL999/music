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
    path('', rankingView, name='ranking'),
    path('.list', RankingList.as_view(), name='rankingList'),
]
