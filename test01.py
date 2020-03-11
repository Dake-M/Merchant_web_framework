# -*- coding: utf-8 -*-
# @Project  :merchant_web_framework
# @File     :test01
# @Date     :2019/12/26 17:25
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm

# f = open(r"C:\Users\saokemo\Desktop\text.txt", "r")
# # f_contains = f.read()
# # print(f_contains)
# f_line = f.readlines()
# print(f_line)
# print(f_line.__len__())
#
# f.close()
#
# f = open(r"C:\Users\saokemo\Desktop\text.txt", 'w')
# for i in f_line:
#     if "180" in i:
#         f.write()

# with open(r"C:\Users\saokemo\Desktop\text.txt", 'r+', encoding='utf-8') as f:
#     f_line = f.readlines()
#     # print(f_line)
#     print(f_line.__len__())
#     list1 = []
#     for i in f_line:
#         if "180" in i:
#             i = "18664334600" + i
#             f.write(i)
#     new = f.read()
#     print(new)


f = open(r"C:\Users\saokemo\Desktop\create_order_info", 'r+', encoding='utf-8')
f_line = f.readlines()
f.close()
s = f_line
print(s)

f1 = open(r"C:\Users\saokemo\Desktop\create_order_info1.txt", 'w', encoding='utf-8')
for i in f_line:
    if "170" in i:
        i = "11000000001" + i
        f1.write(i)
    elif "171" in i:
        i = "11000000002" + i
        f1.write(i)
    elif "172" in i:
        i = "11000000003" + i
        f1.write(i)
    elif "173" in i:
        i = "11000000004" + i
        f1.write(i)
    elif "174" in i:
        i = "11000000005" + i
        f1.write(i)
    elif "175" in i:
        i = "11000000006" + i
        f1.write(i)
    elif "176" in i:
        i = "11000000007" + i
        f1.write(i)
    elif "177" in i:
        i = "11000000008" + i
        f1.write(i)
    elif "178" in i:
        i = "11000000009" + i
        f1.write(i)
    elif "179" in i:
        i = "11000000010" + i
        f1.write(i)
    elif "180" in i:
        i = "11000000011" + i
        f1.write(i)
    elif "181" in i:
        i = "11000000012" + i
        f1.write(i)









f1.close()



# with open(r'C:\Users\saokemo\Desktop\text.txt', 'a', encoding='utf-8') as f:
#     f.write()

# file = open(r"C:\Users\saokemo\Desktop\text.txt", "r", encoding='utf-8')
# lines = file.readlines()
# file.close()
# file = open(r"C:\Users\saokemo\Desktop\text.txt", 'w', encoding='utf-8')
# for k in enumerate(lines):
#     if "180" in lines:
#         file.write('18664334600'%(k))
# file.close()