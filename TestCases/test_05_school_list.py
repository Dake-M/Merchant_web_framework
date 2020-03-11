# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :test_05_student_list
# @Date     :2019/12/19 15:43
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import pytest


@pytest.mark.usefixtures("init_school_list")
class SchoolList:
    """
    学校列表
    """
    def test01_title_info(self, init_school_list):
        """
        页面左上角标题校验
        :return:
        """
        pass