# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :login_datas
# @Date     :2019/10/14 14:10
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm

# 运营商登录非正常数据
merchant_user = [
    {"user": "", "pwd": "", "check": "请输入账号"},
    {"user": "", "pwd": "13222222222", "check": "请输入账号"},
    {"user": "13222222222", "pwd": "", "check": "请输入密码"},
    {"user": "13222222211", "pwd": "13222222222", "check": "账号或密码错误"},
    {"user": "13222222222", "pwd": "13222222211", "check": "账号或密码错误1"},
]