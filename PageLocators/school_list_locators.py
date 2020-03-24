# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :school_list_locators
# @Date     :2019/12/19 15:49
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
from selenium.webdriver.common.by import By


class SchoolList:
    """
    学校列表元素信息
    """
    # ================== 学校列表 ==========================
    # 左上角标题信息
    title_info = (By.XPATH, "//div[@class='info-title']")
    # 搜索文本框
    serch_input_text = (By.XPATH, "//input[@placeholder='请输入学校名称']")
    # 搜按钮
    serch_btn = (By.XPATH, "//button//span[text()='搜索']")
    # 搜索结果
    serch_results = (By.XPATH, "//tbody//td[3]/div")
    # 搜索结果为空
    result_text = (By.XPATH, "//span[@class='el-table__empty-text']")
    # 搜索多结果
    table_group_name = (By.XPATH, "//td[3]//div")
    table_group_name1 = (By.XPATH, "//tr[{}]//td[3]//div")
    # 表头信息
    table_header1 = (By.XPATH, "//thead/tr/th[1]/div")
    table_header2 = (By.XPATH, "//thead/tr/th[2]/div")
    table_header3 = (By.XPATH, "//thead/tr/th[3]/div")
    table_header4 = (By.XPATH, "//thead/tr/th[4]/div")
    table_header5 = (By.XPATH, "//thead/tr/th[5]/div")
    table_header6 = (By.XPATH, "//thead/tr/th[6]/div")
    table_header7 = (By.XPATH, "//thead/tr/th[7]/div")
    # 导出按钮
    export_btn = (By.XPATH, "//button/span[text()='导出']")
    # 列表首行操作列按钮
    school_info_btn = (By.XPATH, "//tbody/tr[1]/td[7]//button/span[text()='详情']")
    school_edit_btn = (By.XPATH, "//tbody/tr[1]/td[7]//button/span[text()='编辑']")
    recover_pwd_btn = (By.XPATH, "//span[text()='重置密码']")
    # 首行列表学校信息
    school_name_text = (By.XPATH, "//tbody/tr/td[3]/div")
    school_type_text = (By.XPATH, "//tbody/tr/td[5]/div")
    school_user_text = (By.XPATH, "//tbody/tr/td[6]/div")
    # 学校详情页面title
    school_info_title = (By.XPATH, "//div[@class='info-title']")
    # 学校详情页面信息
    school_info_name = (By.XPATH, "//span[contains(.,'学校名称：')]/following-sibling::span")
    school_info_type = (By.XPATH, "//span[contains(.,'学校类型：')]/following-sibling::span")
    # 学校编辑页面信息
    school_title = (By.XPATH, "//div[@class='info-title']")
    school_name = (By.XPATH, "//label[@for='schoolName']/following-sibling::div/div")
    school_type = (By.XPATH, "//label[@for='schoolLevel']/following-sibling::div/div")
    school_user = (By.XPATH, "//label[@for='linkMobile']/following-sibling::div/div")
    dow_btn = (By.XPATH, "(//i[contains(@class,'icon el-icon-arrow-up')])[1]")
    type_items = (By.XPATH, "/html/body/div[2]//ul/li")
    type_item = (By.XPATH, "/html/body/div[2]//ul/li[{}]")
    save_btn = (By.XPATH, "//span[text()='保存']")
    # 点击重置密码确定按钮
    pwd_btn = (By.XPATH, "//span[contains(.,'确定')]")
    pwd_recover_tip = (By.XPATH, "//p[contains(@class,'el-message__content')]")


