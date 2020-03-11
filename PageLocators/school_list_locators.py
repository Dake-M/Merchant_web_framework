# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :school_list_locators
# @Date     :2019/12/19 15:49
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
from selenium.webdriver.common.by import By


class SchoolList:
    """
    学校列表元素信息
    """
    # ================== 学校列表 ==========================
    # 左上角标题信息
    title_info = (By.XPATH, "//div[@class='info-title']")