'''
-*- coding: utf-8 -*-
@Time    : 2021/6/9 22:34
@Author  : Luzixuan
@File    : login_datas.py
@contest    : 登录测试数据
'''

# 正常场景用例
success_data = [{"title":"登录成功",
                 "number":"13129080384",
                 "password":"123456",
                 "code":"!@#$"}]

# 异常场景用例
wrong_data = [
    {"title":"账号不存在",
     "number":"131290804",
     "password":"123456",
     "code":"!@#$","except":"手机号码/登录名或密码错误"},
    {"title":"密码错误",
     "number": "131290804",
     "password": "1234",
     "code": "!@#$", "except": "手机号码/登录名或密码错误"},
    {"title":"验证码错误",
     "number": "131290804",
     "password": "123456",
     "code": "cccf", "except": "验证码输入错误！"}
]

if __name__ == '__main__':
    print(success_data[0]["number"])