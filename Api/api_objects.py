# -*- coding: utf-8 -*-
import requests
import warnings


class ApiFunction:
    """
    web自动化前置条件直接调用接口实现的封装
    """
    def __init__(self):
        warnings.filterwarnings("ignore")
        url = "https://payexp.snsshop.net/boss/login/do"
        data = {"username": "13266816551", "password": "123456"}
        self.s = requests.Session()  # 创建session会话
        res = self.s.post(url, data, verify=False)
        # res_json = res.json()
        self.login_key = res.json()["data"]["loginKey"]
        # self.headers = {"login-key": self.login_key}

    def add_bank(self):
        """
        新增银行
        :return:
        """
        url = "https://payexp.snsshop.net/boss/bank-info/create"
        data = {
            "name": "dake_test",
            "bankNo": "dake001",
            "pid": 0
        }
        headers = {"login-key": self.login_key}
        res = self.s.post(url, json=data, headers=headers, verify=False)
        res_json = res.json()
        bank_name = res_json["data"]["name"]
        bank_id = res_json["data"]["id"]
        return bank_name, bank_id


if __name__ == '__main__':
    a = ApiFunction()
    aa = a.add_bank()
    print(aa)

