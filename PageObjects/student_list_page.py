# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :student_list_page
# @Date     :2019/12/13 13:25
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import time
from PageLocators.student_list_locators import StudentList as sl
from Common.BasePage import BasePage


class StudentListPage(BasePage):
    """
    学生列表
    """
    def get_title_info(self):
        """
        获取title_info
        :return:
        """
        time.sleep(1)
        title_text = self.get_element_text(sl.title_info, "获取title文案")
        return title_text

    def get_table_header(self):
        """
        取表头字段信息
        :return:
        """
        table1_header1 = self.get_element_text(sl.table1_header1, "取列表头信息")
        table1_header2 = self.get_element_text(sl.table1_header2, "取列表头信息")
        table1_header3 = self.get_element_text(sl.table1_header3, "取列表头信息")
        table1_header4 = self.get_element_text(sl.table1_header4, "取列表头信息")
        table1_header5 = self.get_element_text(sl.table1_header5, "取列表头信息")
        table1_header6 = self.get_element_text(sl.table1_header6, "取列表头信息")
        return table1_header1, table1_header2, table1_header3, table1_header4, table1_header5, table1_header6

    def search_school_by_name(self, search_school_name):
        """
        根据学校名称搜索列表信息
        :return:
        """
        self.web_refresh()
        self.input_text(search_school_name, sl.input_shcool_name, "输入学校名称")
        self.click_element(sl.search_btn, "点击搜索按钮")
        time.sleep(1)

    def search_school_by_group(self, search_school_group):
        """
        根据分组名称搜索列表信息
        :param search_school_group:
        :return:
        """
        self.web_refresh()
        self.input_text(search_school_group, sl.input_group_name, "输入分组名称")
        self.click_element(sl.search_btn, "点击搜索按钮")
        time.sleep(1)

    def get_school_names(self):
        """
        获取学校名称列表
        :return: 返回学校名称列表
        """
        l = self.get_elements(sl.table_school_name, "获取当前页列表中学校名称的列表并以list返回")
        names = []
        if l.__len__() == 0:
            """
            判断返回的l长度是否为0
            为0则表示搜索不到信息，取搜索不到信息提示的文本值
            不为0则表示搜索到信息，取搜索到信息的对应字段值以列表形式返回
            """
            time.sleep(1)
            result_text = self.get_element_text(sl.result_text, "获取搜索无结果显示的文本值")
            return result_text
        else:
            for i in range(1, l.__len__()+1):
                new_loc = (sl.table_school_name[0], sl.table_school_name[1].format(i))
                text = self.get_element_text(new_loc, "列表中学校名称文本值")
                names.append(text)
            return names  # 以列表形式返回学校名称

    def get_group_names(self):
        """
        获取分组名称列表
        :return: 返回分组名称列表
        """
        l = self.get_elements(sl.table_group_name, "获取当前页列表中分组名称的列表并以list返回")
        names = []
        if l.__len__() == 0:
            """
            判断返回的l长度是否为0
            为0则表示搜索不到信息，取搜索不到信息提示的文本值
            不为0则表示搜索到信息，取搜索到信息的对应字段值以列表形式返回
            """
            time.sleep(1)
            result_text = self.get_element_text(sl.result_text, "获取搜索无结果显示的文本值")
            return result_text
        else:
            for i in range(1, l.__len__()+1):
                new_loc = (sl.table_group_name1[0], sl.table_group_name1[1].format(i))
                text = self.get_element_text(new_loc, "列表中分组名称文本值")
                names.append(text)
            return names  # 以列表形式返回学校名称

    def search_school(self, search_school_name):
        self.web_refresh()
        self.input_text(search_school_name, sl.input_shcool_name, "输入学校名称")
        self.click_element(sl.search_btn, "点击搜索按钮")
        time.sleep(1)

    def get_student_count(self, search_school_name):
        self.search_school(search_school_name)
        text = self.get_element_text(sl.student_count, "获取学生数量文本框")
        return text

    def into_school(self):
        """
        进入学校详情页面
        :return:
        """
        self.click_element(sl.detail_btn, "点击详情按钮")
        time.sleep(1)

    def get_table2_header(self):
        """
        取学校详情页面表头字段信息
        :return:
        """
        table2_header1 = self.get_element_text(sl.table2_header1, "取列表头信息")
        table2_header2 = self.get_element_text(sl.table2_header2, "取列表头信息")
        table2_header3 = self.get_element_text(sl.table2_header3, "取列表头信息")
        table2_header4 = self.get_element_text(sl.table2_header4, "取列表头信息")
        table2_header5 = self.get_element_text(sl.table2_header5, "取列表头信息")
        table2_header6 = self.get_element_text(sl.table2_header6, "取列表头信息")
        table2_header7 = self.get_element_text(sl.table2_header7, "取列表头信息")
        table2_header8 = self.get_element_text(sl.table2_header8, "取列表头信息")
        table2_header9 = self.get_element_text(sl.table2_header9, "取列表头信息")
        return table2_header1, table2_header2, table2_header3, table2_header4, table2_header5, table2_header6, \
               table2_header7, table2_header8, table2_header9

    def get_new_student_count(self):
        text = self.get_element_text(sl.new_student_count, "获取列表总数量")
        return text

    def school_search_student_by_name(self, search_student_name):
        """
        学校详情页面根据学生姓名搜索学生
        :return:
        """
        self.input_text(search_student_name, sl.input_student_name, "输入学生姓名")
        self.click_element(sl.school_search_btn, "点击搜索按钮")
        time.sleep(1)

    def school_search_student_by_id(self, search_school_name, search_student_id):
        """
        学校详情页面根据学生证件号搜索学生
        :return:
        """
        self.web_refresh()
        self.input_text(search_student_id, sl.input_student_id, "输入学生证件号")
        self.click_element(sl.school_search_btn, "点击搜索按钮")
        time.sleep(1)

    def get_student_names(self):
        """
        获取学生姓名列表
        :return: 返回学生姓名列表
        """
        if self.if_ele_is_exist(sl.table_school_name, "元素是否在页面存在"):
            """
            判断元素是否存在
            T则表示搜索不到信息，取搜索不到信息提示的文本值
            F则表示搜索到信息，取搜索到信息的对应字段值以列表形式返回
            """
            l = self.get_elements(sl.table_school_name, "获取当前页列表中学校名称的列表并以list返回")
            names = []
            for i in range(1, l.__len__()+1):
                new_loc = (sl.table_school_name[0], sl.table_school_name[1].format(i))
                text = self.get_element_text(new_loc, "列表中学校名称文本值")
                names.append(text)
            return names  # 以列表形式返回学校名称
        else:
            time.sleep(1)
            result_text = self.get_element_text(sl.result_text, "获取搜索无结果显示的文本值")
            return result_text

    def get_student_ids(self):
        """
        获取学生证件号列表
        :return: 返回学生证件号列表
        """
        l = self.get_elements(sl.table_student_id, "获取当前页列表中学生证件号的列表并以list返回")
        ids = []
        if l.__len__() == 0:
            """
            判断返回的l长度是否为0
            为0则表示搜索不到信息，取搜索不到信息提示的文本值
            不为0则表示搜索到信息，取搜索到信息的对应字段值以列表形式返回
            """
            time.sleep(1)
            result_text = self.get_element_text(sl.result_text, "获取搜索无结果显示的文本值")
            return result_text
        else:
            for i in range(1, l.__len__()+1):
                new_loc = (sl.table_student_id1[0], sl.table_student_id1[1].format(i))
                text = self.get_element_text(new_loc, "列表中学生证件号文本值")
                ids.append(text)
            return ids  # 以列表形式返回学生证件号



