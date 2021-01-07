from time import sleep
from selenium import webdriver
import unittest
import sys,logging
import pytest
from kx_uitest_project.pages.kexin_first_page import Kexin_First_Page
from selenium.webdriver.common.action_chains import ActionChains

def test_first_page(dr):
  dr.find_element_by_css_selector('div.header-con.ivu-layout-header > div > a > i').click() #侧边栏
  dr.find_element_by_css_selector('div.custom-content-con > div.about').click()   #关于
  dr.find_element_by_css_selector('div.ivu-modal-confirm-footer > button').click()  #关闭关于
  sleep(1)
  dr.find_element_by_link_text('语言').click()
  dr.find_element_by_css_selector('div.ivu-select-dropdown > ul > li:nth-child(2)').click() #语言简体
  dr.find_element_by_css_selector('div.user-avator-dropdown > div > div.ivu-dropdown-rel').click()
  dr.find_element_by_css_selector('div.ivu-select-dropdown > ul > li').click()  #点击退出
  sleep(1)
  now_url = dr.current_url
  print(now_url)
  assert 'login' in now_url

if __name__ =='__main__':
  pytest.main()
