# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :test_03_student_list_page
# @Date     :2019/12/13 10:12
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import pytest
from TestDatas import student_list_datas as sld


@pytest.mark.demo
@pytest.mark.usefixtures("init_student_list")
class TestStudentList:
    """
    学生列表页面
    """
    def test01_title_info(self, init_student_list):
        """
        页面左上角标题校验
        :return:
        """
        try:
            assert "学生管理" in init_student_list.get_title_info()
        except Exception as e:
            raise e

    def test02_table_header(self, init_student_list):
        """
        校验表头字段信息
        :return:
        """
        table_headers = init_student_list.get_table_header()
        try:
            assert "学校名称" in table_headers[0]
            assert "分组" in table_headers[1]
            assert "年级数量" in table_headers[2]
            assert "班级数量" in table_headers[3]
            assert "学生数量" in table_headers[4]
            assert "操作" in table_headers[5]
        except Exception as e:
            raise e

    def test03_search_school_by_name(self, init_student_list):
        """
        通过学校名称搜索学校
        :return:
        """
        init_student_list.search_school_by_name(sld.search_school_name)
        names = init_student_list.get_school_names()
        if isinstance(names, list):
            try:
                for item in names:
                    assert sld.search_school_name in item
            except Exception as e:
                raise e
        else:
            assert "暂无数据" in names

    def test04_search_school_by_group(self, init_student_list):
        """
        通过分组名称搜索学校
        :return:
        """
        init_student_list.search_school_by_group(sld.search_group_name)
        names = init_student_list.get_group_names()
        if isinstance(names, list):
            try:
                for item in names:
                    assert sld.search_group_name in item  # 校验搜索关键字是否在列表中的每项都存在
            except Exception as e:
                raise e
        else:
            assert "暂无数据" in names

    def test05_into_school_detail(self, init_student_list):
        """
        进入学校详情页面
        :return:
        """
        student_count = init_student_list.get_student_count(sld.school_name)
        init_student_list.into_school()
        new_count_text = init_student_list.get_new_student_count()
        table2_headers = init_student_list.get_table2_header()
        try:
            assert sld.school_name in init_student_list.get_title_info()  # 校验title_info
            assert student_count in new_count_text  # 校验学生数量
            # 校验列表字段信息
            assert "姓名" == table2_headers[0]
            assert "性别" == table2_headers[1]
            assert "证件类型" == table2_headers[2]
            assert "证件号码" == table2_headers[3]
            assert "年级" == table2_headers[4]
            assert "班级" == table2_headers[5]
            assert "绑定状态" == table2_headers[6]
            assert "父/母姓名" == table2_headers[7]
            assert "联系电话" == table2_headers[8]
        except Exception as e:
            raise e

    def test06_school_search_student_by_name(self, init_student_list):
        """
        在学校详情页面根据学生姓名搜索
        :return:
        """
        init_student_list.school_search_student_by_name(sld.student_name)
        names = init_student_list.get_student_names()
        if isinstance(names, list):
            try:
                for item in names:
                    assert sld.student_name in item
            except Exception as e:
                raise e
        else:
            try:
                assert "暂无数据" in names
            except Exception as e:
                raise e

    def test07_school_search_student_by_id(self, init_student_list):
        """
        在学校详情页面根据学生证件号搜索
        :return:
        """
        init_student_list.school_search_student_by_id(sld.school_name, sld.student_id)
        ids = init_student_list.get_student_ids()
        if isinstance(ids, list):
            try:
                for item in ids:
                    assert sld.student_id in item
            except Exception as e:
                raise e
        else:
            assert "暂无数据" in ids


if __name__ == '__main__':
    pytest.main()
