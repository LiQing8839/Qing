#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 13:42
# @Author  : Qing
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]