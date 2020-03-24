# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :Random
# @Date     :2020/3/23 10:04
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import random
import string


random_int = random.randint(0, 9)
random_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(random_int)
print(random_str)