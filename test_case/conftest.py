from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="session")
def dr():
    url = 'http://iot.szkexin.com.cn:9998'
    dr = webdriver.Chrome()
    dr.get(url)
    dr.maximize_window()
    dr.implicitly_wait(10)
    dr.find_element_by_css_selector('div:nth-child(2) > div > div > input').send_keys('hy')
    dr.find_element_by_css_selector(' div:nth-child(3) > div > div > input').send_keys('a123456')
    dr.find_element(By.CSS_SELECTOR,'div:nth-child(5) > div > label > span > input').click()
    dr.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/form/div[4]/div/div[1]/input').send_keys('huny')
    dr.find_element_by_css_selector('div:nth-child(6) > div > button').click()
    name =  dr.find_element_by_css_selector('div.user-avator-dropdown > div > div.ivu-dropdown-rel').text
    print(name)
    assert 'hy'  in name
    yield dr
    dr.quit()

