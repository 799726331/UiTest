'''
-*- coding: utf-8 -*-
@Time    : 2021/6/9 14:21
@Author  : Luzixuan
@File    : index_page.py
@contest    : 首页页面
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.indexpage_locators import IndexPageLocator as IL

class IndexPage:
    # 首页页面类
    def __init__(self,driver):
        self.driver = driver
    # 判断是否成功登录
    def isExist_success_login_ele(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IL.success_login_ele))
            return True
        except:
            return False
    # 壹链盟产品介绍页入口
    def elimen_enter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IL.elimen_enter_ele))
        self.driver.find_element(*IL.elimen_enter_ele).click()

