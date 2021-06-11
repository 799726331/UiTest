'''
-*- coding: utf-8 -*-
@Time    : 2021/6/10 10:49
@Author  : Luzixuan
@File    : indexpage_locators.py
@contest    : 首页页面元素定位
'''
from selenium.webdriver.common.by import By

class IndexPageLocator:
    # 首页定位类
    # 判断是否成功登录的元素
    success_login_ele = (By.XPATH,'//div[@class="nav-user-info nav-item clearfix"]')
    # 产品介绍页入口
    elimen_enter_ele = (By.XPATH,'//div[@class="img is-not-admin"]')