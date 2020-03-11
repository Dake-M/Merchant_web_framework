# -*- coding: utf-8 -*-
import time
import random
from PageLocators.student_list_locators import StudentList as sl
# for i in range(1,1):
#     print(i)

# def get_school_names(self):
#     """
#     获取学校名称列表
#     :return:
#     """
#     self.input_text("Gander", sl.input_shcool_name, "输入学校名称")
#     self.click_element(sl.search_btn, "aaaa")
#     time.sleep(1)
#     l = self.get_elements(sl.tabel_shcool_name, "获取元素学校名称列表")
#     print(l.__len__())
#     names = []
#     for i in range(1, l.__len__() + 1):
#         new_loc = (sl.tabel_shcool_name1[0], sl.tabel_shcool_name1[1].format(i))
#         text = self.get_element_text(new_loc, "取值")
#         names.append(text)
#     print(names)

# encoding=utf-8

# str=input("输入字段：")
str = 'lxs,hqq,lj,xc'
List = str.split(',')
print(List)

# str_xml=input("输入替换的模板：")
str_xml = '<step id="xml_set_xml_value" comment="value" isrun="true"><param id="xml">VAR_XML</param><param id="xpath">' \
          '//MbfBody/value</param><param id="value">COLUMN(VALUE,y)</param></step>'


# 列表追加，回车成多行
def add_xml(L):
    xml_list = []
    s1 = '\n'  # 回车换行符
    for value in L:
        VAULE = value.upper()
        xml = str_xml.replace('value', value, 2).replace('VALUE', VAULE, 1)  # 替换模板中的值为列表中的值，小写两次，大写一次
        xml_list.append(xml)
    xml_str = s1.join(xml_list)  # list 更新成str
    return xml_str


# 字符串追加，一行
# def add_xml(L):
#   xml_list=''
#   for value in L:
#     VAULE=value.upper()
#     xml= str_xml.replace('value',value,2).replace('VALUE',VAULE,1) #替换模板中的值为列表中的值，小写两次，大写一次
#     xml_list+=xml
#   # xml_str=s1.join(xml_list) #list 更新成str
#   return xml_list

test = add_xml(List)
print(test)


# import time
#
# orderId = ''
# s1 = "\n"
# #
# for ID in range(1, 5):
#     item1 = "<item>" + \
#             "<orderID>" + str(ID) + "</orderID>" + \
#             "<time>" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "</time>" + \
#             "</item>"
#
#     orderId += item1
# messge = "<MbfBody>" + orderId + "</MbfBody> "
# print(messge)