# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Mike Zhou
# @Email : 公众号：测试开发技术
# @File : run_test_html.py
# @Project: 第28课时

'''
遍历测试用例，并生成测试报告
'''

import os
import time
import unittest
from kx_uitest_project.lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case')
    suite = unittest.defaultTestLoader.discover(path, pattern='test*.py')

    # 设置verbosity = 2，并生成HTML测试报告
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


