from selenium import webdriver
import unittest
import sys
import time
from HTMLTestRunner import HTMLTestRunner
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
    

  def test_lock(self):
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/a/i').click()#点击侧边栏
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/li[4]').click()#点击设备管理
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/button[2]').click()#点击数据导出
    time.sleep(1)
    self.driver.find_element_by_xpath('//div[@class="ivu-modal" and @style="width: 500px;"]/div/a/i').click()#点击关闭
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/button/span').click()#点击高级搜索
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/input').click()#点击区域搜索
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span/ul/li[19]').click()#点击广东
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span/span/ul/li[3]').click()#点击深圳
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/span/span/span/ul/li[5]').click()#点击龙岗区
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/span').click()#点击使用状态搜索框
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/ul[2]/li[2]').click()#点击预使用
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div/span').click()#点击在线状态搜索
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/ul[2]/li[1]').click()#点击在线
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[1]/div/span').click()#点击电量搜索框
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div[2]/ul[2]/li[1]').click()#点击1-10
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[1]/div/input').click()#点击创建时间搜索框
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[1]/div[2]/span[1]/em').click()#点击1号
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[1]/div[2]/span[28]/em').click()#点击28
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[4]/button[3]/span').click()#点击确定
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[6]/button').click()#点击查询
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div[7]/button/span').click()#点击重置

    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/input').send_keys('cs')#搜索框输入
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div').click()#点击搜索
    time.sleep(2)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[1]/i').click()#点击...
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[2]/ul/button[1]/span').click()#点击远程开锁
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[2]/ul/button[3]/span').click()#点击详情
    time.sleep(1)
    self.driver.find_element_by_xpath('//div[@class="ivu-modal" and @style="width: 750px;"]/div/div[2]/div[2]/button/span').click()#点击编辑
    time.sleep(1)
    self.driver.find_element_by_xpath('//div[@class="ivu-modal" and @style="width: 750px;"]/div/div[2]/div[2]/button/span').click()#点击保存
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[1]/i').click()#点击...
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[4]/div/div[5]/div[2]/table/tbody/tr[1]/td[1]/div/div/div/div[2]/ul/button[4]/span').click()#点击定位地图
    time.sleep(1)

    self.driver.quit()
if __name__ =='__main__':

  testunit = unittest.defaultTestLoader.discover("/", pattern="iot_*.py")
  


  fp = open('./i.html','wb')
  runner = HTMLTestRunner(stream=fp,title='科信云测试报告',description='用例执行情况')

  runner.run(testunit)
  fp.close()

  unittest.main()
