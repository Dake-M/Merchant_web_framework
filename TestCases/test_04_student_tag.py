# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :test04_student_tag_page
# @Date     :2019/12/16 14:00
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import pytest

from TestDatas import student_tag_datas as std


@pytest.mark.usefixtures("init_student_tag")
class TestStudentTag:
    """
    学生标签
    """
    def test01_title_info(self, init_student_tag):
        """
        页面左上角标题校验
        :return:
        """
        try:
            "今日缴费情况" in init_student_tag.get_title_info()
        except Exception as e:
            raise e

    def test02_table_header(self, init_student_tag):
        """
        学生标签列表表头字段校验
        :return:
        """
        table_headers = init_student_tag.get_table_headers()
        try:
            assert table_headers[0] == "序号"
            assert table_headers[1] == "标签名称"
            assert table_headers[2] == "学生数量"
            assert table_headers[3] == "标签来源"
            assert table_headers[4] == "操作"
        except Exception as e:
            raise e

    def test03_add_tag_title_info(self, init_student_tag):
        """
        新增标签title_info校验
        :return:
        """
        title_info = init_student_tag.get_add_tag_title_info()
        try:
            assert "新增标签" == title_info
        except Exception as e:
            raise e

    def test04_normal_add_tag(self, init_student_tag):
        """
        正常添加/删除标签
        :return:
        """
        init_student_tag.add_tag(std.normal_tag_data["tag_name"])
        try:
            # 添加校验
            assert std.normal_tag_data["check"] in init_student_tag.get_add_msg()
            assert std.normal_tag_data["tag_name"] == init_student_tag.get_tag_name()[0]
            assert "教育局" == init_student_tag.get_tag_name()[1]
        except Exception as e:
            raise e
        finally:
            del_msg = init_student_tag.del_msg_box()
            init_student_tag.del_tag()
            try:
                # 删除校验
                assert del_msg == "确认是否删除该学生标签？删除后，该标签下的学生也会被移除。"
                assert init_student_tag.get_add_msg() == "删除成功!"
            except Exception as e:
                raise e

    @pytest.mark.parametrize("unnormal_tag_data", std.unnormal_tag_data)
    def test05_unnormal_add_tag(self, unnormal_tag_data, init_student_tag):
        """
        非正常添加标签（标签名为空）
        :return:
        """
        init_student_tag.unnormal_add_tag(unnormal_tag_data["tag_name"])
        try:
            assert unnormal_tag_data["check"] in init_student_tag.get_add_msg()
        except Exception as e:
            raise e

    def test06_tag_title_info(self, init_student_tag):
        """
        校验标签学生列左上角title_info和列表为空的提示文案
        :return:
        """
        init_student_tag.add_and_into_tag(std.normal_tag_data["tag_name"])  # 添加并进入标签学生列表
        msg_text = init_student_tag.get_tag_title_info()  # 获取title_info文本值
        try:
            assert msg_text[0] == "学生标签 > 学生列表"  # 校验title_info文本值
            assert msg_text[1] == "暂无数据"  # 校验列表为空提示文案
        except Exception as e:
            raise e

    def test07_import_student(self, init_student_tag):
        """
        标签导入学生列表
            前提条件：
                1、有学校
                2、学校有学生
        :return:
        """
        init_student_tag.import_student(std.import_student)  # 导入学生
        try:
            assert "导入成功" == init_student_tag.get_import_tip()  # 校验导入提示
        except Exception as e:
            raise e

    @pytest.mark.parametrize("school_name", std.school_name)
    def test08_search_by_school_name(self, school_name, init_student_tag):
        """
        标签中根据学校搜索
        :return:
        """
        init_student_tag.search_by_school(school_name["name"])
        result = init_student_tag.get_school_names()
        if isinstance(result, list):
            # 判断返回的结果是否为列表（T表示搜索到数据，F标识搜索不到数据）
            try:
                for item in result:
                    assert school_name["check"] in item
            except Exception as e:
                raise e
        else:
            try:
                assert school_name["check"] == result
            except Exception as e:
                raise e

    @pytest.mark.parametrize("student_name", std.student_name)
    def test09_search_by_student_name(self, student_name, init_student_tag):
        """
        标签中根据学校搜索
        :return:
        """
        init_student_tag.search_by_student(student_name["name"])
        result = init_student_tag.get_student_names()
        if isinstance(result, list):
            # 判断返回的结果是否为列表（T表示搜索到数据，F标识搜索不到数据）
            try:
                for item in result:
                    assert student_name["check"] in item
            except Exception as e:
                raise e
        else:
            try:
                assert student_name["check"] == result
            except Exception as e:
                raise e

    def test10_remove_student_tip_text(self, init_student_tag):
        """
        移除学生弹窗文案校验
        :return:
        """
        text = init_student_tag.get_remove_tip_text()  # 获取弹出文案
        try:
            assert "确认将该学生从当前标签中移除？" == text
        except Exception as e:
            raise e

    def test11_remove_student(self, init_student_tag):
        """
        移除一个学生
            前提条件：
                列表数据超过1条（count > 1）
        :return:
        """
        student_id = init_student_tag.get_student_id()  # 获取学生证件号
        init_student_tag.remove_student()  # 移除学生
        text = init_student_tag.get_remove_tip()  # 获取移除提示
        new_student_id = init_student_tag.get_student_id()
        try:
            assert "操作完成" == text  # 校验提示信息
            assert student_id != new_student_id  # 校验移除后首行的学生证件号不一致
        except Exception as e:
            raise e

    def test12_remove_all_students(self, init_student_tag):
        """
        移除全部学生
        :return:
        """
        init_student_tag.remove_all_students()  # 移除全部学生
        msg_text = init_student_tag.get_table_empty_msg()  # 获取列表为空的提示文案
        try:
            assert "暂无数据" == msg_text
        except Exception as e:
            raise e
        finally:
            init_student_tag.go_back_and_del_tag()  # 删除测试后遗留下来的数据


if __name__ == '__main__':
    pytest.main()




