# -*- coding: utf-8 -*-
import os
import time
import pytest
from selenium import webdriver
from Api.api_objects import ApiFunction
from Common.Conf import Config
from Common.DIR import CONFIGS_DIR
from Common.MYSQL import MySql
from TestDatas import Common_Data as cd
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from PageObjects.student_list_page import StudentListPage
from PageObjects.student_tag_page import StudentTagPage
from PageLocators.home_page_locators import HomeLocs as hl


@pytest.fixture(scope="function")
def login_driver():
    """
    登录页面前后置
    :return:
    """
    driver = webdriver.Chrome()
    driver.get(cd.login_merchant_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    hp = HomePage(driver)

    yield lp, hp

    driver.quit()


@pytest.fixture(scope="class")
def home_driver():
    """
    登录
    :return:
    """
    driver = webdriver.Chrome()
    driver.get(cd.login_merchant_url)
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.merchant_login(cd.merchant_user["user"], cd.merchant_user["pwd"])  # 登录运营商
    hp = HomePage(driver)

    yield hp, driver

    driver.quit()


@pytest.fixture(scope="class")
def init_student_list(home_driver):
    time.sleep(1)
    home_driver[0].click_element(hl.student_menu, "点击学生管理")
    time.sleep(1)
    home_driver[0].click_element(hl.student_list_menu, "点击学生列表")
    slp = StudentListPage(home_driver[1])

    yield slp


@pytest.fixture(scope="class")
def init_student_tag(home_driver):
    time.sleep(1)
    home_driver[0].click_element(hl.student_menu, "点击学生管理")
    time.sleep(1)
    home_driver[0].click_element(hl.student_tag_menu, "点击学生标签")
    slp = StudentTagPage(home_driver[1])

    yield slp





