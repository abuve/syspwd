"""syspwd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^accounts/login/$', login),
    url(r'^passwd_update/$', passwd_update),
    url(r'^login_action/$', account_login),
    url(r'^update_list/$', update_list),
    url(r'^user_add/$', user_add),
    url(r'^get_data/$', get_data),
    url(r'^prompt/$', prompt),
    url(r'^userdel/$', userdel),
    url(r'^download/$', download),
]
