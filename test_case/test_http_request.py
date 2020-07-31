# -*-coding: utf8 -*-


import sys
import os
sys.path.append(".")
sys.path.append("..")
sys.path.append("utils")

#添加环境变量防止出错
import unittest
from ddt import ddt,data
from utils.project_path import *
from utils import read_excel
from utils import read_config
from utils import http_request

cookie = None
test_data = read_excel.Read_the_excel.get_data(test_case_path,config_path)

@ddt()
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        res = http_request.Http_request.http_request(item['url'],
        eval(item['data']),
        item['method'])

        if res.cookies:
            pass
        try:
            self.assertEqual(item['expected'],res.json()['info'])
            
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'FAILED'
            print('执行用例出错：{}'.format(e))
            raise e
        finally:
            #写回功能暂定
            print('获取的结果为{}'.format(res.json()))

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()