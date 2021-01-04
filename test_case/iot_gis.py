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
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[2]/div/div/input').send_keys('YJCtest')
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[3]/div/div/input').send_keys('A123456')
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[5]/div/label/span/input').click()
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[4]/div/div[1]/input').send_keys('huny')
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[6]/div/button').click()
    u = 'http://iot.szkexin.com.cn:9998/home'
    time.sleep(5)
    now_url = self.driver.current_url
    print(now_url)
    self.assertEqual(u,now_url,msg='登陆失败')
    

  def test_GIS1(self):#GIS地图
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/a/i').click()#点击侧边栏
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[2]').click()#点击GIS地图
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/div').click()#点击省级区域
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/ul/li/div').click()#点击市级区域
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/ul/li/ul/li/div').click()#点击第一个区域
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/ul/li/ul/li[1]/ul/li[1]').click()#点击第一个设备
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="allmap"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button[1]').click()#点击设备详情
    time.sleep(1)
    self.driver.find_element_by_xpath('/html/body/div[14]/div[2]/div/div/div[2]/div[2]/button/span').click()#点击关闭
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="allmap"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button[3]').click()#点击远程开锁
    time.sleep(1)
    
    #派发工单

    
    gong = self.driver.find_element_by_xpath('//*[@id="allmap"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button[4]').get_attribute('class')
    print(gong)
    #self.driver.find_element_by_xpath('//*[@id="allmap"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button[4]').click()#点击工单派发
    # time.sleep(3)
    # self.driver.find_element_by_xpath('//tr[@class="ivu-table-row"]/td/div/span').click()#点击用户
    # time.sleep(1)
    # self.driver.find_element_by_xpath('//button[@type="button" and @class="ivu-btn ivu-btn-default" and @style="margin-right: 20px;"]/../button[2]/span').click()#点击确认派发
    # time.sleep(3)

    self.driver.find_element_by_xpath('//*[@id="allmap"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button[5]').click()#点击查看图片
    time.sleep(1)
    self.driver.find_element_by_xpath('//div[@class="ivu-modal" and @style="width: 520px;"]/div/a/i').click()#点击关闭
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="allmap"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button[6]').click()#点击日志
    time.sleep(1)
    #回到地图设备界面
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[2]').click()#点击GIS地图
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/div').click()#点击省级区域
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/ul/li/div').click()#点击市级区域
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/ul/li/ul/li/div').click()#点击第一个区域
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/ul/li/ul/li/ul/li[1]/ul/li[1]').click()#点击第一个设备
    time.sleep(3)
    # self.driver.find_element_by_xpath('//*[@id="allmap"]/div[1]/div/div[2]/div/div[2]/div/div[1]/button[7]').click()#点击告警处理
    # time.sleep(1)

    self.driver.quit()

if __name__ =='__main__':
  unittest.main()
