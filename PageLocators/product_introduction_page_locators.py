'''
-*- coding: utf-8 -*-
@Time    : 2021/6/10 15:22
@Author  : Luzixuan
@File    : product_introduction_page_locators.py
@contest    : 产品介绍页定位元素
'''

from selenium.webdriver.common.by import By

class ProductIntroduction:
    # 产品中心tab按钮
    Introduction_Button = (By.XPATH,'//a[@class="router-link-exact-active router-link-active is-hot"]')
    # 产业金融服务tab按钮
    Introduction_money_Button = (By.XPATH,'//div[text()="产业金融服务"]')
    # 融e拆迁按钮
    RONGECHAIQIAN_Button = (By.XPATH,'//a[text()="融e拆迁"]')