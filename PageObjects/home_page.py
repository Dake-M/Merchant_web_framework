# -*- coding: utf-8 -*-
import time
from PageLocators.home_page_locators import HomeLocs as hl
from Common.BasePage import BasePage


class HomePage(BasePage):
    """
    运营商首页
    """
    def get_merchant_name(self):
        """
        获取运营商名称
        :return:
        """
        time.sleep(1)
        merchant_name = self.get_element_text(hl.merchant_name, "左上角运营商名称")
        return merchant_name

    def get_user(self):
        """
        获取右上角帐号
        :return:
        """
        time.sleep(1)
        user = self.get_element_text(hl.user, "获取登录账号")
        return user

    def get_title_info(self):
        """
        获取页面title信息
        :return:
        """
        time.sleep(1)
        title_text = self.get_element_text(hl.title_info, "获取title文案")
        return title_text

    def get_box1_msg(self):
        """
        获取box1文案信息
        :return:
        """
        box_msg = self.get_element_text(hl.box_msg1, "获取box1_msg文案")
        return box_msg

    def get_box2_msg(self):
        """
        获取box2文案信息
        :return:
        """
        box_msg = self.get_element_text(hl.box_msg2, "获取box1_msg文案")
        return box_msg

    def get_box3_msg(self):
        """
        获取box3文案信息
        :return:
        """
        box_msg = self.get_element_text(hl.box_msg3, "获取box1_msg文案")
        return box_msg

    def get_box4_msg(self):
        """
        获取box4文案信息
        :return:
        """
        box_msg = self.get_element_text(hl.box_msg4, "获取box1_msg文案")
        return box_msg

    def get_tab1_attr(self):
        """
        获取tab1元素的"tabindex"值
        tabindex为0：高光到这个tab
        tabindex为1：高光到其他tab
        :return:
        """
        tab_index = self.get_element_attr(hl.table1, "tabindex", "获取tab1元素属性值")
        return tab_index

    def get_tab2_attr(self):
        """
        获取tab2元素的"tabindex"值
        tabindex为0：高光到这个tab
        tabindex为1：高光到其他tab
        :return:
        """
        tab_index = self.get_element_attr(hl.table2, "tabindex", "获取tab2元素属性值")
        return tab_index

    def get_table1_cell2(self):
        """
        获取table1表格第二列字段名称
        :return:
        """
        cell_text = self.get_element_text(hl.table1_cell2, "获取table1表格第二列字段名称")
        return cell_text

    def get_table1_cell5(self):
        """
        获取table1表格第五列字段名称
        :return:
        """
        cell_text = self.get_element_text(hl.table1_cell5, "获取table1表格第五列字段名称")
        return cell_text

    def change_tab(self):
        """
        切换tab到分组总览
        :return:
        """
        self.click_element(hl.table2, "点击分组总览")
        time.sleep(1)

    def get_table2_cell2(self):
        """
        获取table2表格第二列字段名称
        :return:
        """
        cell_text = self.get_element_text(hl.table2_cell2, "获取table2表格第二列字段名称")
        return cell_text

    def get_table2_cell5(self):
        """
        获取table2表格第五列字段名称
        :return:
        """
        cell_text = self.get_element_text(hl.table2_cell5, "获取table2表格第五列字段名称")
        return cell_text

    def quit_login(self):
        """
        退出登录
        :return:
        """
        self.move_mouse(hl.user, "鼠标移动到帐号上面")
        time.sleep(1)
        self.click_element(hl.quit_btn, "点击退出按钮")
        time.sleep(1)

