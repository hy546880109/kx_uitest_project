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
    self.driver.implicitly_wait(10)
  def test_login(self):
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

 # def test_alarm(self):#告警管理
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/a/i').click()#点击侧边栏
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[3]/span').click()#点击告警管理
    time.sleep(3)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/input').send_keys('cs')#搜索框输入cs
    
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div').click()#点击搜索
   
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/input').clear()#清除搜索框
  
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button/span').click()#点击高级搜索
  
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/button[2]/span').click()#点击重置
	  
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/input').click()#点击区域搜索框
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span/ul/li[19]').click()#点击广东
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span/span/ul/li[3]').click()#点击深圳
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span/span/span/ul/li[5]').click()#点击龙岗区
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/span').click()#点击设备类型搜查框
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/ul[2]/li').click()#点击应急包
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div/span').click()#点击告警类型搜索框
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/ul[2]/li[2]').click()#点击低电量
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[1]/div/span').click()#点击告警状态搜索框
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[2]/ul[2]/li[1]').click()#点击告警
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/button[1]/span').click()#点击搜索
    time.sleep(3)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/button[2]/span').click()#点击重置
   # time.sleep(3)
   # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[1]/i').click()#点击...
   # time.sleep(1)
   # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[3]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[2]/ul/button[2]/span').click()#点击快速处理
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[1]/i').click()#点击...
    
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[2]/ul/button[3]/span').click()#点击定位地图
    
    self.driver.find_element_by_css_selector('#app > div > div.ivu-layout > div.main-content-con.ivu-layout-content > div > div > div > ul > li.ivu-page-next > a > i').click()#点击下一页
    self.driver.quit()
if __name__ =='__main__':
  unittest.main()