# -*- coding: utf-8 -*-
import pytest
from TestDatas import Common_Data as cd
from TestDatas import login_datas as ld


@pytest.mark.usefixtures("login_driver")
class TestLogin:
    """
    运营商登录
    """
    def test01_merchant_login_success(self, login_driver):
        """
        运营商正常登录
        :return:
        """
        login_driver[0].merchant_login(cd.merchant_user["user"], cd.merchant_user["pwd"])
        try:
            assert login_driver[1].get_merchant_name() == "兴和网络测试"
            assert cd.merchant_user["user"] in login_driver[1].get_user()
        except Exception as e:
            raise e

    def test02_merchant_login_unverify(self, login_driver):
        """
        运营商登录不滑动验证
        :return:
        """
        login_driver[0].merchant_login_unverify(cd.merchant_user["user"], cd.merchant_user["pwd"])
        try:
            assert login_driver[0].get_error_msg() == "请拖动验证滑块"
        except Exception as e:
            raise e

    @pytest.mark.parametrize("merchant_user", ld.merchant_user)
    def test03_merchant_login_unnormale(self, merchant_user, login_driver):
        """
        运营商非正常登录
        :return:
        """
        login_driver[0].merchant_login(merchant_user["user"], merchant_user["pwd"])
        try:
            assert login_driver[0].get_error_msg() == merchant_user["check"]
        except Exception as e:
            raise e


if __name__ == '__main__':
    pytest.main()