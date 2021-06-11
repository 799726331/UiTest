'''
-*- coding: utf-8 -*-
@Time    : 2021/6/10 15:31
@Author  : Luzixuan
@File    : chose_product_page.py
@contest    : 
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.product_introduction_page_locators import ProductIntroduction as PI

class ChoseProductPage:
    def __init__(self,driver):
        self.driver = driver
    # 进入融e拆迁产品主页
    def rongechaiqian_enter(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PI.Introduction_Button))
        pass
