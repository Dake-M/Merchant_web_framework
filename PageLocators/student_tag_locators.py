# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :student_tag
# @Date     :2019/12/16 14:07
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
from selenium.webdriver.common.by import By


class StudentTag:
    """
    学生标签页面元素管理
    """
    # ================== 学生标签列表 ==========================
    # 左上角标题信息
    title_info = (By.XPATH, "//div[@class='info-title']")
    # 标签列表字段信息
    table_header1 = (By.XPATH, "//th[1]//div[1]")
    table_header2 = (By.XPATH, "//th[2]//div[1]")
    table_header3 = (By.XPATH, "//th[3]//div[1]")
    table_header4 = (By.XPATH, "//th[4]//div[1]")
    table_header5 = (By.XPATH, "//th[5]//div[1]")
    # 添加标签按钮
    add_tag_btn = (By.XPATH, "//button//span[text()='添加标签']")
    # 列表首行标签名称
    tag_name = (By.XPATH, "//tr[1]//td[2]")
    # 列表首行标签来源
    tag_source = (By.XPATH, "//tr[1]//td[4]")
    # 列表首行标签学生列表按钮
    student_btn = (By.XPATH, "//tr[1]//button//span[contains(text(),'学生列表')]")
    # 列表首行编辑标签按钮
    edit_btn = (By.XPATH, "//tr[1]//button//span[contains(text(),'编辑标签')]")
    # 列表首行删除按钮
    del_btn = (By.XPATH, "//tr[1]//button//span[contains(text(),'删除')]")
    # 删除确定按钮
    del_action = (By.XPATH, "//button//span[contains(text(),'确定')]")
    # 删除提示信息
    del_msg = (By.XPATH, "//div[@class='el-message-box__message']//p")
    # 删除提示
    del_tip = (By.XPATH, "//p[@class='el-message__content']")

    # ================== 新增学生标签列表 ==========================
    # 新增标签页面左上角title_info
    left_header = (By.XPATH, "//div[@class='el-dialog__header']")
    # 标签名文本框
    input_tag_name = (By.XPATH, "//label[contains(.,'标签名称')]/following-sibling::div//input")
    # 添加确定按钮
    action_btn = (By.XPATH, "//button//span[text()='确 定']")
    # 添加提示信息
    add_msg = (By.XPATH, "//p[@class='el-message__content']")

    # ================== 学生标签列表 ==========================
    # 学生列表页面title_info
    tag_title_info = (By.XPATH, "//div[@class='info-title']")
    # 导入按钮
    import_btn = (By.XPATH, "//button//span[text()='导入']")
    # 导入图标
    import_img = (By.XPATH, "//i[@class='el-icon-upload']")
    # 导入提示
    import_tip = (By.XPATH, " //p[@class='el-message__content']")
    # 列表为空文案提示
    table_empty = (By.XPATH, "//span[@class='el-table__empty-text']")
    # 学校文本框
    input_school_name = (By.XPATH, "//input[@placeholder='请输入学校名称']")
    # 学生姓名文本框
    input_student_name = (By.XPATH, "//input[@placeholder='请输入姓名']")
    # 搜索按钮
    search_btn = (By.XPATH, "//button//span[text()='搜索']")
    # 列表数据为空
    result_text = (By.XPATH, "//span[@class='el-table__empty-text']")
    # 列表中学校名称
    table_school_names = (By.XPATH, "//td[6]/div[1]")
    table_school_names1 = (By.XPATH, "//tr[{}]/td[6]/div[1]")
    # 列表中学生姓名
    table_student_names = (By.XPATH, "//td[2]/div[1]")
    table_student_names1 = (By.XPATH, "//tr[{}]/td[2]/div[1]")
    # 列表首行学生证件号
    student_id = (By.XPATH, "//tr[1]/td[5]/div[1]")
    # 列表全选框
    all_select_box = (By.XPATH, "//th[contains(@class,'is-leaf')]//span[@class='el-checkbox__inner']")
    # 列表首行选择框
    select_box = (By.XPATH, "//tr[1]/td[1]/div[1]/label[1]/span[1]/span[1]")
    # 移除按钮
    remove_btn = (By.XPATH, "//button[@class='el-button color_b el-button--danger el-button--small']")
    # 移除提示窗口
    remove_tip_text = (By.XPATH, "//div[@class='el-message-box__message']//p")
    # 移除确定按钮
    remove_action_btn = (By.XPATH, "//span[contains(text(),'确定')]")
    # 移除提示文案
    remove_tip = (By.XPATH, "//p[@class='el-message__content']")
    # 移除后列表提示
    tag_table_empty = (By.XPATH, "//span[@class='el-table__empty-text']")




