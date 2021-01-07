# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术
# @File : baidu_page.py
# @Project: 第34课时

from page_objects import PageElement, PageObject  #引入库

class KexinHomePage(PageObject):
    '''登陆界面'''
    home_username_input = PageElement(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[2]/div/div/input')
    home_password_input = PageElement(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[3]/div/div/input')
    home_jizhu_Options = PageElement(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[5]/div/label/span/input')
    home_auth_input = PageElement(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[4]/div/div[1]/input')
    home_login_buttun = PageElement(xpath='//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[6]/div/button')