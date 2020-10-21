# -*-coding: utf8 -*-

'''
runner.py
运行测试用例并生成测试报告

'''
import os
import unittest
from HtmlTestRunner import HTMLTestRunner
from test_case.test_http_request import TestHttpRequest
from utils import init_path
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
#说明：unittest.TestLoader().loadTestsFromTestCase(类名)
file_name = init_path.report_path
with open(file_name,"w",encoding="utf-8") as f :
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        output="./report/",
        report_title="api_test_report",
        report_name="test_api测试报告",
        add_timestamp=False,    #取消命名时间戳
        open_in_browser=True    #浏览器自动打开
    )
    runner.run(suite)
    


