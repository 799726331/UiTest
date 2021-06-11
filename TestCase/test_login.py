'''
-*- coding: utf-8 -*-
@Time    : 2021/6/9 15:27
@Author  : Luzixuan
@File    : test_login.py
@contest    : 测试用例
'''
import unittest
from selenium import webdriver
from PageObject import login_page
from PageObject import index_page
from Testdatas.Common_datas import CommonDatas as cd
from Testdatas import login_datas as ld
import ddt

@ddt.ddt()
class TestLogin(unittest.TestCase):
    # 每一个类开始执行前运行一次
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cd.web_login_url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.lg = login_page.LoginPage(cls.driver)
    # 每一个类开始执行后运行一次
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    # 前置条件,每一个函数开始前运行一次
    def setUp(self):
        pass
    # # 后置条件,每一个函数结束后运行一次
    def tearDown(self):
        self.driver.refresh()

    # 手机号码错误
    @ddt.data(*ld.wrong_data)
    def test_login_000_user_wrongFormat(self,data):
        self.lg.login(data["number"],data["password"],data["code"])
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(),data["except"])
    # 正常登录
    def test_login_001(self):
        self.lg.login(ld.success_data[0]["number"],ld.success_data[0]["password"],ld.success_data[0]["code"])
        reqs = index_page.IndexPage(self.driver).isExist_success_login_ele()
        self.assertTrue(reqs,"正常登录失败")

    # 密码错误
    # def test_login_user_wrongFormat_002(self):
    #     number = "13129080304"
    #     password = "1234"
    #     code = "!@#$"
    #     self.lg.login(number,password,code)
    #     self.assertEqual(self.lg.get_errorMsg_from_loginArea(),"手机号码/登录名或密码错误")
    # #验证码错误
    # def test_login_user_wrongFormat_003(self):
    #     number = "131290804"
    #     password = "123456"
    #     code = "cccf"
    #     self.lg.login(number,password,code)
    #     self.assertEqual(self.lg.get_errorMsg_from_loginArea(),"验证码输入错误！")




if __name__ == '__main__':
    unittest.main(verbosity=2)