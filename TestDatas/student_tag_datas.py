# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :student_tag_datas
# @Date     :2019/12/17 11:27
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
from Common.DIR import case_dir

# 新增标签数据信息
normal_tag_data = {"tag_name": "dake_tag", "check": "添加成功"}
unnormal_tag_data = [
    {"tag_name": "", "check": "标签名称不能为空"},
    {"tag_name": "三好生", "check": "标签已存在"}
]

# 运营商标签学生导入模版地址
import_student = case_dir + "\学生标签导入模板(教育局).xlsx"

# 标签通过学校名称搜索
school_name = [
    {"name": "Gander", "check": "Gander"},
    {"name": "dake", "check": "暂无数据"}
]
# 标签通过学生姓名搜索
student_name = [
    {"name": "汪", "check": "汪"},
    {"name": "dake", "check": "暂无数据"}
]


