# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :school_list_page
# @Date     :2019/12/19 15:48
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import time
import random
import string
from Common.LOAD_FILE import WinUpLoadFile
from PageLocators.school_list_locators import SchoolList as schl
from Common.BasePage import BasePage


class SchoolListPage(BasePage):
    """
    学校列表
    """
    def get_title_info(self):
        """
        获取左上角title信息
        :return:
        """
        time.sleep(1)
        title_text = self.get_element_text(schl.title_info, "获取title文案")
        return title_text

    def get_table_headers(self):
        """
        获取列表头字段信息
        :return:
        """
        table_header1 = self.get_element_text(schl.table_header1, "取列表字段信息")
        table_header2 = self.get_element_text(schl.table_header2, "取列表字段信息")
        table_header3 = self.get_element_text(schl.table_header3, "取列表字段信息")
        table_header4 = self.get_element_text(schl.table_header4, "取列表字段信息")
        table_header5 = self.get_element_text(schl.table_header5, "取列表字段信息")
        table_header6 = self.get_element_text(schl.table_header6, "取列表字段信息")
        table_header7 = self.get_element_text(schl.table_header7, "取列表字段信息")
        return table_header1, table_header2, table_header3, table_header4, table_header5, table_header6, table_header7

    def serch_school(self, school_name):
        """
        搜索学校操作
        """
        self.web_refresh()
        self.input_text(school_name, schl.serch_input_text, "输入学校名称")
        self.click_element(schl.serch_btn, "点击搜索按钮")
        time.sleep(1)

    def get_school_names(self):
        """
        获取搜索列表学校名称集合
        :return:
        """
        l = self.get_elements(schl.table_group_name, "获取当前页列表中学校名称的列表并以list返回")
        names = []
        if l.__len__() == 0:
            """
            判断返回的l长度是否为0
            为0则表示搜索不到信息，取搜索不到信息提示的文本值
            不为0则表示搜索到信息，取搜索到信息的对应字段值以列表形式返回
            """
            time.sleep(1)
            result_text = self.get_element_text(schl.serch_results, "获取搜索无结果显示的文本值")
            return result_text
        else:
            for i in range(1, l.__len__() + 1):
                new_loc = (schl.table_group_name1[0], schl.table_group_name1[1].format(i))
                text = self.get_element_text(new_loc, "列表中分组名称文本值")
                names.append(text)
            return names  # 以列表形式返回学校名称

    def export_schools(self):
        """
        导出学校
        :return:
        """
        self.click_element(schl.export_btn, "点击导出按钮")
        time.sleep(2)

    def get_school_list_info(self):
        """
        获取学校列表首行信息
        :return:
        """
        school_list = []
        school_name = self.get_element_text(schl.school_name_text, "获取首行学校名称")
        school_type = self.get_element_text(schl.school_type_text, "获取首行学校类型")
        school_user = self.get_element_text(schl.school_user_text, "获取首行学校帐号")
        school_list.append(school_name)
        school_list.append(school_type)
        school_list.append(school_user)
        return school_list

    def into_school_info(self):
        """
        进入学校详情操作
        :return:
        """
        time.sleep(1)
        self.click_element(schl.school_info_btn, "点击操作列详情按钮")

    def get_school_info(self):
        """
        进入详情获取学校信息
        :return:
        """
        info_list = []
        time.sleep(1)
        school_info_title = self.get_element_text(schl.school_info_title, "获取学校详情页面title文案")
        school_info_name = self.get_element_text(schl.school_info_name, "获取学校详情页面学校名称文案")
        school_info_type = self.get_element_text(schl.school_info_type, "获取学校详情页面学校类型文案")
        info_list.append(school_info_title)
        info_list.append(school_info_name)
        info_list.append(school_info_type)
        return info_list

    def go_back(self):
        """
        返回上一页
        :return:
        """
        self.go_back()
        time.sleep(1)

    def into_edit_school(self):
        """
        返回学校列表点击编辑进入编辑页面
        :return:
        """
        self.click_element(schl.school_edit_btn, "点击操作列编辑按钮")
        time.sleep(1)

    def get_edit_info(self):
        """
        获取学校编辑页面信息
        :return:
        """
        info_list = []
        edit_title = self.get_element_text(schl.school_title, "获取编辑页面title信息")
        school_name = self.get_element_text(schl.school_name , "获取编辑页面学校名称")
        school_type = self.get_element_text(schl.school_type , "获取编辑页面学校类型")
        school_user = self.get_element_text(schl.school_user , "获取编辑页面学校帐号")
        info_list.append(edit_title)
        info_list.append(school_name)
        info_list.append(school_type)
        info_list.append(school_user)
        return info_list

    def edit_school(self, new_school_name):
        """
        编辑学校信息
            学校名称：
            学校类型：
        :return:
        """
        self.input_clear(schl.school_name, "清除学校名称文本框原名称")
        self.input_text(new_school_name, schl.school_name, "输入新的学校名称")
        self.click_element(schl.dow_btn, "点击学校类型下拉框")
        time.sleep(1)
        l = self.get_elements(schl.type_items, "获取当前页列表中学校名称的列表并以list返回")
        new_school_type = (schl.type_item[0], schl.type_item[1].format(random.randint(1, l.__len__())))
        text = self.get_element_text(new_school_type, "获取学校类型名称")
        self.click_element(new_school_type, "选择学校类型点击")
        self.click_element(schl.save_btn, "点击保存按钮")
        return text

    def recover_pwd(self):
        """
        重置密码
        :return:
        """
        self.click_element(schl.recover_pwd_btn, "点击重置密码按钮")
        self.click_element(schl.pwd_btn, "点击确定重置按钮")

    def get_recover_pwd_tip(self):
        """
        获取充值密码成功提示
        :return:
        """
        return self.get_element_text(schl.pwd_recover_tip, "获取重置密码成功提示语")

















