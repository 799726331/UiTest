'''
-*- coding: utf-8 -*-
@Time    : 2021/6/9 14:21
@Author  : Luzixuan
@File    : login_page.py
@contest    : 登录页面
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocator as loc

class LoginPage:
    # 登录页面类
    def __init__(self,driver):
        self.driver = driver
    def login(self,number,password,code):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.number_value))
        self.driver.find_element(*loc.number_value).send_keys(number)
        self.driver.find_element(*loc.password_value).send_keys(password)
        self.driver.find_element(*loc.code_value).send_keys(code)
        self.driver.find_element(*loc.login_button).click()
    # 注册入口
    def register_enter(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.register_button))
        self.driver.find_element(*loc.register_button).click()
    # 忘记密码
    def forget_password(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.forget_password_button))
        self.driver.find_element(*loc.forget_password_button).click()
    #获取错误信息-登录区域
    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.error_message))
        return self.driver.find_element(*loc.error_message).text