# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :test_05_student_list
# @Date     :2019/12/19 15:43
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import pytest


@pytest.mark.usefixtures("init_school_list")
class TestSchoolList:
    """
    学校列表
    """
    def test01_title_info(self, init_school_list):
        """
        页面左上角标题校验
        :return:
        """
        try:
            assert "学校列表" in init_school_list.get_title_info()
        except Exception as e:
            raise e

    def test02_table_info(self, init_school_list):
        """
        表头信息校验
        :param init_school_list:
        :return:
        """
        table_headers = init_school_list.get_table_headers()
        try:
            assert table_headers[0] == "序号"
            assert table_headers[1] == "学校logo"
            assert table_headers[2] == "学生名称"
            assert table_headers[3] == "分组"
            assert table_headers[4] == "学校类型"
            assert table_headers[5] == "学校帐号"
            assert table_headers[6] == "操作"
        except Exception as e:
            raise e

    def test03_serch_school(self, init_school_list):
        """
        学校搜索
        :param init_school_list:
        :return:
        """
        init_school_list.serch_school("七期中心学校")
        names = init_school_list.get_school_names()
        for i in range(names.__len__()):
            try:
                assert "七期中心学校" in names[i]
            except Exception as e:
                raise e

    def test04_school_info(self, init_school_list):
        """
        学校详情页面信息校验
        :param init_school_list:
        :return:
        """
        school_info1 = init_school_list.get_school_list_info()
        init_school_list.init_school_list()
        school_info2 = init_school_list.get_school_info()
        try:
            assert "七期中心学校" in school_info2[0]
            assert school_info1[0] == school_info2[1]
            assert school_info1[1] == school_info2[2]
        except Exception as e:
            raise e

    def test05_into_edit_school(self, init_school_list):
        """
        进入学校编辑页面校验信息
        :param init_school_list:
        :return:
        """
        init_school_list.go_back()
        info = init_school_list.get_school_list_info()
        init_school_list.into_edit_school()
        info1 = init_school_list.get_edit_info()
        try:
            assert "七期中心学校" in info1[0]
            assert info[0] == info1[1]
            assert info[1] == info1[2]
            assert info[2] == info1[3]
        except Exception as e:
            raise e

    def test06_edit_school(self, init_school_list, new_school_name):
        """
        编辑学校信息
            学校名称：
            学校类型：
        :param init_school_list:
        :return:
        """
        type = init_school_list.edit_school(new_school_name)
        init_school_list.serch_school(new_school_name)
        info = init_school_list.get_school_list_info()
        try:
            assert new_school_name == info[0]
            assert type == info[1]
        except Exception as e:
            raise e

    def test07_recoover_pwd(self, init_school_list):
        """
        重置密码
        :param init_school_list:
        :return:
        """
        init_school_list.serch_school("七期中心学校")
        init_school_list.recover_pwd()
        tip = init_school_list.get_recover_pwd_tip()
        try:
            assert tip == "重置成功!"
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()











