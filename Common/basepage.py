'''
-*- coding: utf-8 -*-
@Time    : 2021/6/11 10:23
@Author  : Luzixuan
@File    : basepage.py
@contest    : 
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocator as loc

# 封装基本函数  执行日志,异常处理,失败截图
# 所有的页面公共操作的部分
class BasePage:
    def __init__(self,driver):
        self.driver = driver
    # 等待元素可见
    def wait_eleVisible(self):
        pass
    # 等待元素存在
    def wait_elePresence(self):
        pass
    # 查找元素
    def get_element(self):
        pass
    # 点击操作
    def click_element(self):
        pass
    # 输入操作
    def input_text(self):
        pass
    # 获取元素的文本内容
    def get_text(self):
        pass
    # 获取元素属性
    def get_element_attribute(self):
        pass
    # alert处理
    def alert_action(self):
        pass
    # iframe切换
    def switch_iframe(self):
        pass
    #上传操作
    def upload_file(self):
        pass

