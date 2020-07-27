# -*-coding: utf8 -*-

'''
project_path.py
实现路径的可配置，避免使用相对路径，防止出错

'''
import os

# 获取当前目录的最大路径
project_path =os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试数据的路径
if not os.path.exists(project_path + r'\data'):
    os.mkdir(project_path + r'\data')
test_case_path = os.path.join(project_path,'data','data_http.xlsx')

#测试报告路径
if not os.path.exists(project_path + r'\report'):
    os.mkdir(project_path + r'\report')
report_path = os.path.join(project_path,'report','test_http_report.html')

#配置文件路径
if not os.path.exists(project_path + r'\config'):
    os.mkdir(project_path + r'\config')
config_path = os.path.join(project_path,'config','http_case.config')
