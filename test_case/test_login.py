from selenium import webdriver
import unittest
import sys,os,time
import ddt
from kx_uitest_project.common.browser import Browser
from kx_uitest_project.pages.kexin_home_page import KexinHomePage
from kx_uitest_project.common.parse_excel import ParseExcel
import logging

# 登陆

def get_test_data():
    '''
    从外部获取参数数据
    :return:
    '''
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_data')
    excelPath = os.path.join(path, 'test_baidu_search.xlsx')
    sheetName = '搜索关键字'
    return ParseExcel(excelPath, sheetName)

print(get_test_data().getDatasFromSheet())


@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls)-> None: 
        # path = os.path.join(os.path.dirname(
        #     os.path.dirname(os.path.abspath(__file__))), 'lib')
        cls.url = 'http://iot.szkexin.com.cn:9998'
        cls.driver = Browser.open_browser('chrome')
        

    @classmethod
    def tearDownClass(cls)-> None:
        time.sleep(1)
        cls.driver.quit()

    def setUp(self) -> None:
        self.kexin_home = KexinHomePage(self.driver)      
        self.kexin_home.get(self.url)

    @ddt.data(*get_test_data().getDatasFromSheet())
    def test_001_login(self,data):
        '''输入正确的用户名和密码，空的验证码'''
        print('data:',data)
        username, password = tuple(data)
        print('username:',username,'password:', password)
        kexin_home = KexinHomePage(self.driver)
        kexin_home.home_username_input.send_keys(username)
        kexin_home.home_password_input.send_keys(password)
        kexin_home.home_jizhu_Options.click()
        kexin_home.home_auth_input.send_keys('huny')
        kexin_home.home_login_buttun.click()
        now_url = self.driver.current_url
        self.assertNotIn('home',now_url,'失败')


if __name__ == '__main__':
    unittest.main()
