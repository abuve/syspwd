#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 主机密码管理工具
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Title:        views
# Description:  定义主程序执行方法
# Copyright:    Copyright (c) 2015
# @ author : Abuve
# @ version: 1.0
# @ email  : buhe_186@163.com
# @ web    : http://www.abuve.com/
# -------------------------------------------------
# Import python module

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from app.models import *
import os
import sys
import json
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('%s/cores' %BASE_DIR)
# 自定义加密模块
import encrypt

reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.

# 程序首页
@login_required
def index(request):
    user_current = passwd_current.objects.all().order_by('-id')
    return render_to_response('index.html',{'user_current':user_current,'url_tag':'index'})

# 登陆方法
def login(request):
    return render_to_response('login.html')

# 用户验证
def account_login(request):
    username = request.POST['user']
    password = request.POST['passwd']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect("/")
    else:
        return render_to_response('login.html',{'err':'用户或密码错误，请重新输入.'})

# 用户口令更新
@login_required
def passwd_update(request):
    data_tuple = request.POST.lists()
    data_dic = {}
    login_user = request.user.username
    for i in data_tuple:
        data_dic[i[0]] = i[1][0]

    update_user = data_dic['select_user']
    update_passwd = data_dic['password']
    encrypt_passwd = encrypt.encrypt_mode_cbc(update_passwd,encrypt.keys).replace('\n','')
    update_current = passwd_current.objects.filter(user=update_user).all()
		
    if len(update_current) ==1:
        update_current = passwd_current.objects.get(user=update_user)
        update_current.user = update_user
        update_current.passwd = encrypt_passwd
        update_current.author = login_user
        update_current.save()
		
        # update history data.
        update_list = passwd_list()
        update_list.user = update_user
        update_list.passwd = encrypt_passwd
        update_list.author = login_user
        update_list.save()
    else:
        return_data='异常操作，请联系系统管理员!'
        return HttpResponse(return_data)

    update_list = passwd_list.objects.all()
    prompt_data="<h4><b>操作提示：口令修改成功!这是系统最后一次显示所修改的明文口令，请牢记该口令，如需再次获取，请联系系统管理员!</b></h4><h4 style=\"color:red\"><b>用户：%s</b></h4><h4 style=\"color:red\"><b>口令：%s</b></h4>" %(update_user,update_passwd)
    return render_to_response('prompt.html',{'prompt_data':prompt_data})

# 添加用户
def user_add(request):
    data_tuple = request.POST.lists()
    data_dic = {}
    login_user = request.user.username
    for i in data_tuple:
        data_dic[i[0]] = i[1][0]
    update_user = data_dic['useradd_name']
    update_passwd = data_dic['useradd_passwd']
    encrypt_passwd = encrypt.encrypt_mode_cbc(update_passwd,encrypt.keys).replace('\n','')

    update_current = passwd_current.objects.filter(user=update_user).all()
    if len(update_current) ==0:
        update_current = passwd_current()
        update_current.user = update_user
        update_current.passwd = encrypt_passwd
        update_current.author = login_user
        update_current.save()

        # update history data.
        update_list = passwd_list()
        update_list.user = update_user
        update_list.passwd = encrypt_passwd
        update_list.author = login_user
        update_list.save()
        prompt_data="<h4><b>操作提示：用户创建成功!这是系统最后一次显示所修改的明文口令，请牢记该口令，如需再次获取，请联系系统管理员!</b></h4><h4 style=\"color:red\"><b>用户：%s</b></h4><h4 style=\"color:red\"><b>口令：%s</b></h4>" %(update_user,update_passwd)
        return render_to_response('prompt.html',{'prompt_data':prompt_data})
    else:
        prompt_data="<h4><b>操作提示：用户%s已经存在,请确认后重新操作。</b></h4>" %update_user
        return render_to_response('prompt.html',{'prompt_data':prompt_data})

# 定义客户端Http数据请求方法
def get_data(request):
    if request.method != 'POST':
	    return HttpResponse('You are not allowed to be accessed.')
    data_tuple = request.POST.lists()
    keys = 'custom_your_keys'
    data_dic = {}

    for i in data_tuple:
        data_dic[i[0]] = i[1][0]

    if 'keys' not in data_dic.keys() or 'user' not in data_dic.keys():
        return HttpResponse('You are not allowed to be accessed.')

    if data_dic['keys'] !=keys:
        return HttpResponse('You are not allowed to be accessed.')
    
    username = data_dic['user']
    passwd_data = passwd_current.objects.values('passwd').filter(user=username)

    if len(passwd_data) ==1:
        for i in passwd_data:
            data = i
    elif len(passwd_data) >1:
        # error code 1: system has multi users.
        data = 1
    else:
        # error code 2: system not found user.
        data = 2
    return HttpResponse(json.dumps(data))

# 提示页面
@login_required
def prompt(request):
    return render_to_response('prompt.html',{'url_tag':'index'})

# 用户删除操作
@login_required
def userdel(request):
    username = request.POST['username']
    passwd_current.objects.get(user=username).delete()
    prompt_data="<h4><b>操作提示：用户%s已成功删除。</b></h4>" %username
    return render_to_response('prompt.html',{'prompt_data':prompt_data})

# 用户更新记录
@login_required
def update_list(reuqest):
    update_data = passwd_list.objects.all().order_by('-id')
    return render_to_response('update_list.html',{'update_data':update_data,'url_tag':'index'})

# 程序下载页
@login_required
def download(reuqest):
    return render_to_response('download.html',{'url_tag':'download'})
