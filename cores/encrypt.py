#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 主机密码管理工具
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Title:        Decrypt
# Description:  该模块定义了明文字符串加密方法
# Copyright:    Copyright (c) 2015
# @ author : Abuve
# @ version: 1.0
# @ email  : buhe_186@163.com
# @ web    : http://www.abuve.com/
# -------------------------------------------------
# Import python module

# AES加密模块,对字符串进行加解密
from Crypto.Cipher import AES
from Crypto import Random
# 二进制转换模块
import binascii
# Python常用系统模块
import sys
# 加密签名keys(长度需16位)
keys = 'custom_your_keys'

# 定义密码加密函数
def encrypt_mode_cbc(data, key, iv = keys,base64 = True):
    # 判断密文长度，如不符合16位长度倍数，后补空格
    lenth = len(data)
    num = lenth % 16
    data = data.ljust(lenth + 16 - num)
    # 使用签名keys对明文密码进行ASE算法1级加密
    obj = AES.new(key, AES.MODE_CBC, iv)
    result = obj.encrypt(data)
    # 使用base64算法进行2级加密，如base64方法为False，使用十六进制进行转义
    return result.encode('base64') if base64 is True else result.encode('hex')

if __name__ == '__main__':
    input_text = sys.argv[1]
    encrypt = encrypt_mode_cbc(input_text, keys)
    print encrypt
