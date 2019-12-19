# -*- coding: utf-8 -*-
# =================== 登录页面 =================
from selenium.webdriver.common.by import By


class LoginLocs:
    """
    运营商登录页面元素管理
    """
    #  ==================运营商系统==========================
    # 登录账号文本框
    merchant_input_user = (By.XPATH, "//input[@placeholder='账号']")
    # 登录密码文本框
    merchant_input_password = (By.XPATH, "//input[@placeholder='密码']")
    # 滑动图标
    merchant_img = (By.XPATH, "//div[@class='slider-btn']//img")
    # 登录按钮
    merchant_login_btn = (By.XPATH, "//button[@class='el-button userbtn el-button--primary el-button--medium']")
    # 登录错误信息
    error_msg = (By.XPATH, "//p[@class='el-message__content']")
