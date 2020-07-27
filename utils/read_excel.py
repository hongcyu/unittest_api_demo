# -*-coding: utf8 -*-

'''
read_excel.py
读取excel表单内的数据，通过配置文件实现测试用例的配置,只能是xslx

'''

import project_path
from read_config import Read_config
from openpyxl import load_workbook

class Read_the_excel(object):

    @staticmethod
    def get_data(test_case_path):


