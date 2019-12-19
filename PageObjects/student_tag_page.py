# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :student_tag_page
# @Date     :2019/12/16 14:01
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import time
from PageLocators.student_tag_locators import StudentTag as stl
from Common.BasePage import BasePage
from Common.LOAD_FILE import WinUpLoadFile


class StudentTagPage(BasePage):
    """
    学生标签
    """
    def get_title_info(self):
        """
        获取title_info文本值
        :return:
        """
        self.web_refresh()
        text = self.get_element_text(stl.title_info, "获取title_info文本值")
        return text

    def get_table_headers(self):
        """
        获取列表头字段信息
        :return:
        """
        table_header1 = self.get_element_text(stl.table_header1, "取列表字段信息")
        table_header2 = self.get_element_text(stl.table_header2, "取列表字段信息")
        table_header3 = self.get_element_text(stl.table_header3, "取列表字段信息")
        table_header4 = self.get_element_text(stl.table_header4, "取列表字段信息")
        table_header5 = self.get_element_text(stl.table_header5, "取列表字段信息")
        return table_header1, table_header2, table_header3, table_header4, table_header5

    def get_add_tag_title_info(self):
        """
        取添加标签弹窗的title_info
        :return:
        """
        self.web_refresh()
        self.click_element(stl.add_tag_btn, "点击添加标签按钮")
        time.sleep(0.5)
        text = self.get_element_text(stl.left_header, "取弹窗的左上角title_info")
        return text

    def add_tag(self, tag_name):
        """
        正常添加标签
        （当添加删除标签用例单独跑时需要把前面两行注释去掉）
        :param tag_name: 标签名
        :return:
        """
        # self.click_element(stl.add_tag_btn, "点击添加标签按钮")
        # time.sleep(0.5)
        self.input_text(tag_name, stl.input_tag_name, "录入标签名称")
        self.click_element(stl.action_btn, "点击确认按钮")
        time.sleep(0.5)

    def unnormal_add_tag(self, tag_name):
        """
        非正常添加标签
        :return:
        """
        self.web_refresh()
        self.get_add_tag_title_info()
        self.add_tag(tag_name)

    def del_tag(self):
        """
        删除标签
        :return:
        """
        self.click_element(stl.del_action, "点击删除确定按钮")
        time.sleep(0.5)

    def del_msg_box(self):
        """
        获取删除提示信息
        :return:
        """
        self.web_refresh()
        self.click_element(stl.del_btn, "点击删除按钮")
        time.sleep(0.5)
        return self.get_element_text(stl.del_msg, "获取删除提示信息文本")

    def get_add_msg(self):
        """
        添加/删除标签获取提示信息
        :return:
        """
        add_msg = self.get_element_text(stl.add_msg, "获取提示信息")
        return add_msg

    def get_tag_name(self):
        """
        获取列表首行标签名称和标签来源
        :return:
        """
        tag_name = self.get_element_text(stl.tag_name, "获取标签名称")
        tag_source = self.get_element_text(stl.tag_source, "获取标签来源")
        return tag_name, tag_source

    def add_and_into_tag(self, tag_name):
        self.web_refresh()
        self.click_element(stl.add_tag_btn, "点击添加标签按钮")
        time.sleep(0.5)
        self.input_text(tag_name, stl.input_tag_name, "录入标签名称")
        self.click_element(stl.action_btn, "点击确认按钮")
        time.sleep(0.5)
        self.web_refresh()
        self.click_element(stl.student_btn, "点击进入标签学生列表")
        time.sleep(1)

    def into_tag(self):
        """
        进入标签学生列表
        :return:
        """
        self.web_refresh()
        self.click_element(stl.student_btn, "点击进入标签学生列表")
        time.sleep(0.5)

    def get_tag_title_info(self):
        """
        获取tag列表页面title_info和列表为空文本提示
        :return:
        """
        self.web_refresh()
        title_info_text = self.get_element_text(stl.tag_title_info, "获取标签学生列表的左上角title_info")
        table_empty_text = self.get_element_text(stl.table_empty, "获取列表为空文案提示")
        return title_info_text, table_empty_text

    def import_student(self, file_path):
        """
        标签导入学生
        :return:
        """
        self.click_element(stl.import_btn, "点击导入按钮")
        time.sleep(0.5)
        self.click_element(stl.import_img, "点击导入图标")
        time.sleep(0.5)
        WinUpLoadFile().winUpLoadFile(file_path, "打开")
        time.sleep(0.5)

    def get_import_tip(self):
        """
        获取导入提示
        :return:
        """
        return self.get_element_text(stl.import_tip, "获取导入提示")

    def search_by_school(self, school_name):
        """
        根据学校搜索
        :return:
        """
        self.web_refresh()  # 刷新页面
        self.input_text(school_name, stl.input_school_name, "输入学生姓名")
        self.click_element(stl.search_btn, "点击搜索按钮")
        time.sleep(0.5)

    def get_school_names(self):
        """
        获取学校名称列表
        :return: 返回学校名称列表
        """
        if self.if_ele_is_exist(stl.table_school_names, "等待元素在页面存在"):
            """
            判断元素是否存在
            T则表示搜索不到信息，取搜索不到信息提示的文本值
            F则表示搜索到信息，取搜索到信息的对应字段值以列表形式返回
            """
            l = self.get_elements(stl.table_school_names, "获取当前页列表中学校名称的列表并以list返回")
            names = []
            for i in range(1, l.__len__()+1):
                new_loc = (stl.table_school_names1[0], stl.table_school_names1[1].format(i))
                text = self.get_element_text(new_loc, "列表中学校名称文本值")
                names.append(text)
            return names  # 以列表形式返回学校名称
        else:
            time.sleep(1)
            result_text = self.get_element_text(stl.result_text, "获取搜索无结果显示的文本值")
            return result_text

    def search_by_student(self, student_name):
        """
        通过学生姓名搜索
        :param student_name:
        :return:
        """
        self.web_refresh()  # 刷新页面
        self.input_text(student_name, stl.input_student_name, "输入学校名称")
        self.click_element(stl.search_btn, "点击搜索按钮")
        time.sleep(0.5)

    def get_student_names(self):
        """
        获取学生姓名列表
        :return: 返回学生姓名列表
        """
        if self.if_ele_is_exist(stl.table_student_names, "等待元素在页面存在"):
            """
            判断元素是否存在
            T则表示搜索不到信息，取搜索不到信息提示的文本值
            F则表示搜索到信息，取搜索到信息的对应字段值以列表形式返回
            """
            l = self.get_elements(stl.table_student_names, "获取当前页列表中学生姓名的列表并以list返回")
            names = []
            for i in range(1, l.__len__()+1):
                new_loc = (stl.table_student_names1[0], stl.table_student_names1[1].format(i))
                text = self.get_element_text(new_loc, "列表中学生姓名文本值")
                names.append(text)
            return names  # 以列表形式返回学校名称
        else:
            time.sleep(1)
            result_text = self.get_element_text(stl.result_text, "获取搜索无结果显示的文本值")
            return result_text

    def get_student_id(self):
        """
        移除前获取首行学生证件号
        :return:
        """
        self.web_refresh()
        time.sleep(0.5)
        student_name = self.get_element_text(stl.student_id, "获取首行学生证件号")
        return student_name

    def remove_student(self):
        """
        标签移除学生
        :return:
        """
        self.web_refresh()
        time.sleep(0.5)
        self.click_element(stl.select_box, "点击移除选项框")
        self.click_element(stl.remove_btn, "点击移除按钮")
        time.sleep(0.5)
        self.click_element(stl.remove_action_btn, "点击移除确定按钮")
        time.sleep(0.5)

    def get_remove_tip_text(self):
        """
        获取删除弹窗的提示文案
        :return:
        """
        self.web_refresh()
        time.sleep(0.5)
        self.click_element(stl.select_box, "点击移除选项框")
        self.click_element(stl.remove_btn, "点击移除按钮")
        time.sleep(0.5)
        text = self.get_element_text(stl.remove_tip_text, "获取移除弹窗提示文案")
        return text

    def get_remove_tip(self):
        """
        获取移除完成后提示文案
        :return:
        """
        text = self.get_element_text(stl.remove_tip, "获取移除提示信息")
        return text

    def remove_all_students(self):
        """
        移除全部学生
        :return:
        """
        self.web_refresh()
        time.sleep(0.5)
        self.click_element(stl.all_select_box, "勾选全选框")
        self.click_element(stl.remove_btn, "点击移除按钮")
        time.sleep(0.5)
        self.click_element(stl.remove_action_btn, "点击移除确定按钮")
        time.sleep(1)

    def get_table_empty_msg(self):
        self.web_refresh()
        time.sleep(1)
        text = self.get_element_text(stl.tag_table_empty, "获取空表提示文案")
        return text

    def go_back_and_del_tag(self):
        """
        返回上一页并删除标签
        :return:
        """
        self.go_back()
        self.del_msg_box()
        self.del_tag()


















