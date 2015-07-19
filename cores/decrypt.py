#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 主机密码管理工具
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Title:        Decrypt
# Description:  该模块定义了加密字符串解密方法
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
# 加密签名keys
keys = 'custom_your_keys'

# 定义密码解密函数
def decrypt_mode_cbc(encrypted, key, iv = keys, base64 = True):
    # 对加密内容进行1级解密，如未采用base64算法，则采用十六进制算法
    encrypted = encrypted.decode('base64') if base64 is True else encrypted.decode('hex')
    if encrypted is not '':
        # 使用签名keys对1级解密结果采用ASE算法进行2级解密
        obj = AES.new(key, AES.MODE_CBC, iv)
        # 返回解密字符串
        return obj.decrypt(encrypted)
    else:
        return False

# 主程序代码段
if __name__ == '__main__':
    # 判断脚本执行参数
    try:
        if len(sys.argv) > 2:
            print 'You give more arguments. Check it please.'
            print 'Usage: %s (encrypted password)' %sys.argv[0]
            sys.exit()
        else:
            input_text = sys.argv[1]
    except IndexError:
        print 'Usage: %s (encrypted password)' %sys.argv[0]
        sys.exit()
    try:
        decrypt = decrypt_mode_cbc(input_text, keys)
    except:
        print 'Error: Invalid encrypted password, Check it and try again.'
        sys.exit()
    
    # 输出解密后内容，并替除后补空格
    print decrypt.replace(' ','')
