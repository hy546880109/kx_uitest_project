from selenium import webdriver
import unittest
import sys
import time
#登陆
class TestLogin(unittest.TestCase):
  def setUp(self):
    url = 'http://iot.szkexin.com.cn:9998'
    self.driver = webdriver.Chrome()
    self.driver.get(url)
    self.driver.maximize_window()
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys('YJCtest')#应急仓登录帐号
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[3]/div/div/input').send_keys('A123456')
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[5]/div/label/span/input').click()
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[4]/div/div[1]/input').send_keys('huny')
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[6]/div/button').click()
    u = 'http://iot.szkexin.com.cn:9998/home'
    time.sleep(5)
    now_url = self.driver.current_url
    print(now_url)
    self.assertEqual(u,now_url,msg='登陆失败')
    

  def test_user(self):
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/a/i').click()#点击侧边栏
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[7]/div').click()#点击用户
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[7]/ul/li[1]').click()#点击用户管理
    time.sleep(3)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[1]/i').click()#点击...
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[2]/ul/button[1]/span').click()#点击详情
    time.sleep(1)
    self.driver.find_element_by_css_selector('body > div:nth-child(22) > div.ivu-modal-wrap.modal-vertical-center > div > div > div.ivu-modal-body > div:nth-child(2) > button > span').click()#点击编辑
    time.sleep(1)
    self.driver.find_element_by_css_selector('body > div:nth-child(22) > div.ivu-modal-wrap.modal-vertical-center > div > div > div.ivu-modal-body > div:nth-child(2) > button').click()#点击保存
    time.sleep(1)

    self.driver.quit()
if __name__ =='__main__':
  unittest.main()
