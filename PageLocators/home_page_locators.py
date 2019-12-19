# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class HomeLocs:
    """
    运营商首页元素管理
    """
    # 左上角运营商名称
    merchant_name =(By.XPATH, "//span[@class='name']")
    # 右上角帐号
    user = (By.XPATH, "//span[contains(@class,'user-name el-dropdown-selfdefine')]")
    # 帐号下的退出
    quit_btn = (By.XPATH, "//li[text()='退出']")
    # 页面title信息
    title_info = (By.XPATH, "//div[@class='info-title']")
    # 今日收费学校总数
    box_msg1 = (By.XPATH, "//div[@class='content-box back1']//span[@class='text']")
    # 今日缴费人数
    box_msg2 = (By.XPATH, "//div[@class='content-box back2']//span[@class='text']")
    # 今日缴费总金额
    box_msg3 = (By.XPATH, "//div[@class='content-box back3']//span[@class='text']")
    # 当期缴费金额
    box_msg4 = (By.XPATH, "//div[@class='content-box back4']//span[@class='text']")
    # 学校总览
    table1 = (By.XPATH, "//div[@id='tab-1']")
    # 分组总览
    table2 = (By.XPATH, "//div[@id='tab-2']")
    # 学校总览列表 - 学校名称
    table1_cell2 = (By.XPATH, "//th[2]//div[1]")
    # 学校藏蓝列表 - 累计收费金额
    table1_cell5 = (By.XPATH, "//th[5]//div[1]")
    # 分组总览 - 分组名称
    table2_cell2 = (By.XPATH, "//th[2]//div[1]")
    # 分组总览 - 当期收费金额
    table2_cell5 = (By.XPATH, "//th[5]//div[1]")

    # ======================= 菜单 ==========================
    # 学生管理菜单
    student_menu = (By.XPATH, "//span[@slot='title'][contains(.,'学生管理')]")
    # 学生管理菜单 - 学生列表
    student_list_menu = (By.XPATH, "//span[@slot='title'][contains(.,'学生列表')]")
    # 学生管理菜单 - 学生标签
    student_tag_menu = (By.XPATH, "//span[@slot='title'][contains(.,'学生标签')]")
    # 学校管理菜单
    school_menu = (By.XPATH, "//span[@slot='title'][contains(.,'学校管理')]")
    # 学校管理菜单 - 学校列表
    school_list_menu = (By.XPATH, "//span[@slot='title'][contains(.,'学校列表')]")
    # 学校管理菜单 - 分组管理
    school_group_menu = (By.XPATH, "//span[@slot='title'][contains(.,'分组管理')]")
    # 报表中心菜单
    report_menu = (By.XPATH, "//span[contains(.,'报表中心')]")
    # 设置菜单
    setting_menu = (By.XPATH, "//span[@slot='title' and text()='设置']")
    # 设置菜单 - 基本信息
    setting_menu_item1 = (By.XPATH, "//span[@slot='title' and text()='基本信息']")
    # 设置菜单 - 微信小程序
    setting_menu_item2 = (By.XPATH, "//span[@slot='title' and text()='微信小程序']")
    # 设置菜单 - 项目设置
    setting_menu_item3 = (By.XPATH, "//span[@slot='title' and text()='项目设置']")
    # 权限管理菜单
    authority_menu = (By.XPATH, "//span[@slot='title' and text()='权限管理']")
    # 权限管理菜单 - 成员管理
    manager_menu = (By.XPATH, "//span[@slot='title' and text()='成员管理']")
    # 权限管理菜单 - 部门管理
    department_menu = (By.XPATH, "//span[@slot='title' and text()='部门管理']")
    # 权限管理菜单 - 职位管理
    position_menu = (By.XPATH, "//span[@slot='title' and text()='职位管理']")
