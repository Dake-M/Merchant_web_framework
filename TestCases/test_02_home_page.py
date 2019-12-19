# -*- coding: utf-8 -*-
import pytest


@pytest.mark.demo
@pytest.mark.usefixtures("home_driver")
class TestHome:
    """
    运营商首页
    """
    def test01_title_info(self, home_driver):
        """
        页面左上角标题校验
        :return:
        """
        try:
            "今日缴费情况" in home_driver[0].get_title_info()
        except Exception as e:
            raise e

    def test02_box1_msg(self, home_driver):
        """
        box1_msg校验
        :return:
        """
        try:
            "今日收费学校总数" in home_driver[0].get_box1_msg()
        except Exception as e:
            raise e

    def test03_box2_msg(self, home_driver):
        """
        box2_msg校验
        :return:
        """
        try:
            "今日缴费人数" in home_driver[0].get_box2_msg()
        except Exception as e:
            raise e

    def test04_box3_msg(self, home_driver):
        """
        box3_msg校验
        :return:
        """
        try:
            "今日缴费总金额" in home_driver[0].get_box3_msg()
        except Exception as e:
            raise e

    def test05_box4_msg(self, home_driver):
        """
        box4_msg校验
        :return:
        """
        try:
            "当期缴费金额" in home_driver[0].get_box4_msg()
        except Exception as e:
            raise e

    def test06_tab_attr(self, home_driver):
        """
        tab属性值校验
        :param home_driver:
        :return:
        """
        try:
            assert home_driver[0].get_tab1_attr() == "0"
            assert home_driver[0].get_tab2_attr() == "-1"
        except Exception as e:
            raise e

    def test07_table_cell(self, home_driver):
        """
        学校总览表格字段校验
        :return:
        """
        try:
            assert home_driver[0].get_table1_cell2() == "学校名称"
            assert home_driver[0].get_table1_cell5() == "累计收费金额"
        except Exception as e:
            raise e

    def test08_change_tab(self, home_driver):
        """
        切换到分组总览表格
        :return:
        """
        home_driver[0].change_tab()
        try:
            assert home_driver[0].get_tab1_attr() == "-1"
            assert home_driver[0].get_tab2_attr() == "0"
            assert home_driver[0].get_table2_cell2() == "分组名称"
            assert home_driver[0].get_table2_cell5() == "当期收费金额"
        except Exception as e:
            raise e

    def test09_quit_login(self, home_driver):
        """
        退出登录
        :return:
        """
        home_driver[0].quit_login()
        try:
            home_driver[0].get_title() == "登录"
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()



