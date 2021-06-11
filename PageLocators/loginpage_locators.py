'''
-*- coding: utf-8 -*-
@Time    : 2021/6/10 10:48
@Author  : Luzixuan
@File    : loginpage_locators.py
@contest    : 登录页面元素定位
'''
from selenium.webdriver.common.by import By

class LoginPageLocator:
    # 登录定位类
    # 手机号/登录名输入框
    number_value = (By.XPATH, '//div/input[@placeholder="请输入手机号/登录名"]')
    # 密码输入框
    password_value = (By.XPATH, '//div/input[@placeholder="请输入您的登录密码"]')
    # 验证码输入框
    code_value = (By.XPATH, '//div/input[@placeholder="请输入验证码"]')
    # 登录按钮
    login_button = (By.XPATH, '//div/button[@class="el-button login-btn el-button--primary el-button--medium"]')
    # 注册按钮
    register_button = (By.XPATH, '//span[text()="免费注册"]')
    # 忘记密码按钮
    forget_password_button = (By.XPATH, '//span[text()="忘记密码"]')
    # 错误提示框信息内容
    error_message = (By.XPATH, '//div[@class="el-message-box__message"]')