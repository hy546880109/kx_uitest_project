import unittest
import time
from lib.HTMLTestRunner import HTMLTestRunner

now = time.strftime("%Y-%m-%d %H_%M_%S")
test_dir = './'#当前路径
discover = unittest.defaultTestLoader.discover(test_dir, pattern='iot_*.py')#iot_*.py包含测试用例的名称
filename = test_dir  + now + 'iot.html'
fp = open(filename,"wb")#报告存放的路径
runner = HTMLTestRunner(stream=fp, title='科信云测试报告',description='测试用例情况:')
runner.run(discover)
fp.close()