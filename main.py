# -*- coding: utf-8 -*-
# @Project  :Merchant_Web_framework
# @File     :main
# @Date     :2019/12/13 10:07
# @Author   :Dake
# @Email    :6004297158@qq.com
# @Software :PyCharm
import pytest
import warnings

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    pytest.main(["-m", "demo","--html=Outputs/reports/report.html"])
    # pytest.main(["-m", "demo", "--reruns", "2", "--reruns-delay", "5", "--html=Outputs/reports/report.html"])