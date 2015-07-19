#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 主机密码管理工具
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Title:        models
# Description:  定义mysql数据表结构
# Copyright:    Copyright (c) 2015
# @ author : Abuve
# @ version: 1.0
# @ email  : buhe_186@163.com
# @ web    : http://www.abuve.com/
# -------------------------------------------------
# Import python module

from django.db import models
from django.conf import settings

# Create your models here.

class passwd_current(models.Model):
    user = models.CharField(max_length=20)
    passwd = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.user

class passwd_list(models.Model):
    user = models.CharField(max_length=20)
    passwd = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.user
