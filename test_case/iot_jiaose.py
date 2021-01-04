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
    

  def test_jiaose(self):
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/a/i').click()#点击侧边栏
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[7]/div').click()#点击用户
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[7]/ul/li[2]').click()#点击角色管理
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/div/div/div/div[1]/i').click()#点击...
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/table/tbody/tr[1]/td[6]/div/div/div/div[2]/ul/button[2]/span').click()#点击分配权限
    time.sleep(1)
    self.driver.find_element_by_xpath("//div[@class='ivu-modal-wrap modal-vertical-center']//button[@class='ivu-btn ivu-btn-primary ivu-btn-large']").click()#点击确定
    time.sleep(1)

    self.driver.quit()
if __name__ =='__main__':
  unittest.main()
