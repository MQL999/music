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
    path('login.html', loginView, name='login'),
    path('home/<int:page>.html', homeView, name='home'),
    path('logout.html', logoutView, name='logout'),
]
