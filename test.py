# -*- coding: utf-8 -*-
import time
from PageLocators.student_list_locators import StudentList as sl
# for i in range(1,1):
#     print(i)

def get_school_names(self):
    """
    获取学校名称列表
    :return:
    """
    self.input_text("Gander", sl.input_shcool_name, "输入学校名称")
    self.click_element(sl.search_btn, "aaaa")
    time.sleep(1)
    l = self.get_elements(sl.tabel_shcool_name, "获取元素学校名称列表")
    print(l.__len__())
    names = []
    for i in range(1, l.__len__() + 1):
        new_loc = (sl.tabel_shcool_name1[0], sl.tabel_shcool_name1[1].format(i))
        text = self.get_element_text(new_loc, "取值")
        names.append(text)
    print(names)