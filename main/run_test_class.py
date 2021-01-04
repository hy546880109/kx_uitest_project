# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : run_test_class.py
# @Project: 第25课时

'''
按指定类运行测试用例
'''

import os,time
import unittest
from kx_uitest_project.test_case.iot_login import TestLogin
from kx_uitest_project.lib.TestRunner.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':

    # 根据给定的测试类，获取其中所有以test开头的测试方法，并返回一个测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    
    # 将多个测试类加载到测试套件中
    suite = unittest.TestSuite([suite1])

    # 设置verbosity = 2，可以打印出更详细的执行信息
    # unittest.TextTestRunner(verbosity=2).run(suite)

    project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    report_dir = os.path.join(project_root, 'report')
    # 测试报告地址
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_abspath = os.path.join(report_dir, "HTMLReport_{}.html".format(current_time))
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='自动化测试报告',
                                description='用例执行情况',
                                verbosity=2
                                )
        runner.run(suite)