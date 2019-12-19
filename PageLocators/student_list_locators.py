# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class StudentList:
    """
    学生列表元素管理
    """
    # ================== 运营商学生列表 ==========================
    # 左上角标题信息
    title_info = (By.XPATH, "//div[@class='info-title']")
    # 学校名称文本框
    input_shcool_name = (By.XPATH, "//input[@placeholder='请输入学校名称']")
    # 分组名称文本框
    input_group_name = (By.XPATH, "//input[@placeholder='请输入分组名称']")
    # 搜索按钮
    search_btn = (By.XPATH, "//button[@class='el-button el-button--primary el-button--small']")
    # 搜索数据为空文本值
    result_text = (By.XPATH, "//span[@class='el-table__empty-text']")
    # 列表中学校名称列表
    table_school_name = (By.XPATH, "//td[1]//div[1]")
    table_school_name1 = (By.XPATH, "//tr[{}]//td[1]//div[1]")
    # 列表中分组名称列表
    table_group_name = (By.XPATH, "//td[2]//div[1]")
    table_group_name1 = (By.XPATH, "//tr[{}]//td[2]//div[1]")
    # 列表首行详情按钮
    detail_btn = (By.XPATH, "//span[text()='详情']")
    # 学生数量
    student_count = (By.XPATH, "//tr[1]//td[5]//div[1]")
    # 列表头信息
    table1_header1 = (By.XPATH, "//th[1]//div[1]")
    table1_header2 = (By.XPATH, "//th[2]//div[1]")
    table1_header3 = (By.XPATH, "//th[3]//div[1]")
    table1_header4 = (By.XPATH, "//th[4]//div[1]")
    table1_header5 = (By.XPATH, "//th[5]//div[1]")
    table1_header6 = (By.XPATH, "//th[6]//div[1]")

    # ================== 学校详情页面 ==========================
    # 表头信息
    table2_header1 = (By.XPATH, "//th[1]//div[1]")
    table2_header2 = (By.XPATH, "//th[2]//div[1]")
    table2_header3 = (By.XPATH, "//th[3]//div[1]")
    table2_header4 = (By.XPATH, "//th[4]//div[1]")
    table2_header5 = (By.XPATH, "//th[5]//div[1]")
    table2_header6 = (By.XPATH, "//th[6]//div[1]")
    table2_header7 = (By.XPATH, "//th[7]//div[1]")
    table2_header8 = (By.XPATH, "//th[8]//div[1]")
    table2_header9 = (By.XPATH, "//th[9]//div[1]")

    # 学生姓名文本框
    input_student_name = (By.XPATH, "//input[@placeholder='请输入姓名']")
    # 证件号码文本框
    input_student_id = (By.XPATH, "//input[@placeholder='请输入完整证件号或末4位']")
    # 搜索按钮
    school_search_btn = (By.XPATH, "//span[text()='搜索']")
    # 列表中学生姓名列表
    table_student_name = (By.XPATH, "//td[1]//div[1]")
    table_student_name1 = (By.XPATH, "//tr[{}]//td[1]//div[1]")
    # 列表中学生证件号列表
    table_student_id = (By.XPATH, "//td[4]/div")
    table_student_id1 = (By.XPATH, "//tr[{}]//td[4]//div")
    # 学生总数
    new_student_count = (By.XPATH, "//span[@class='el-pagination__total']")