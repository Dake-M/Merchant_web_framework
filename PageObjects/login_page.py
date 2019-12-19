# -*- coding: utf-8 -*-
import time
from PageLocators.login_page_locators import LoginLocs as ll
from Common.BasePage import BasePage


class LoginPage(BasePage):
    """
    运营商登录
    """
    def merchant_login(self, user, pwd):
        """
        运营商登录
        :param user: 账号
        :param pwd: 密码
        :return:
        """
        self.web_refresh()
        self.input_text(user, ll.merchant_input_user, "输入账号")
        self.input_text(pwd, ll.merchant_input_password, "输入密码")
        self.click_move_mouse(ll.merchant_img, "滑动验证")
        self.click_element(ll.merchant_login_btn, "点击登录按钮")
        time.sleep(1)

    def merchant_login_unverify(self, user, pwd):
        """
        非正常登录
            （不滑动验证）
        :param user: 账号
        :param pwd: 密码
        :return:
        """
        self.web_refresh()
        self.input_text(user, ll.merchant_input_user, "输入账号")
        self.input_text(pwd, ll.merchant_input_password, "输入密码")
        self.click_element(ll.merchant_login_btn, "点击登录按钮")
        time.sleep(0.5)

    def get_error_msg(self):
        """
        获取错误信息
        :return:
        """
        error_msg = self.get_element_text(ll.error_msg, "获取错误提示信息")
        return error_msg


