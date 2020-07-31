# -*-coding: utf8 -*-

'''
project_path.py
实现路径的可配置，避免使用相对路径，防止出错

'''
import os
import time
# 获取当前目录的最大路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试数据的路径
if not os.path.exists(project_path + r'\data'):
    os.mkdir(project_path + r'\data')
test_case_path = os.path.join(project_path,'data','data_http.xlsx')

#测试报告路径
if not os.path.exists(project_path + r'\report'):
    os.mkdir(project_path + r'\report')
##以时间命名
# t = time.localtime()
# t = time.strftime(r"_%m_%d_%H_%M_%S",t)
#report_path = os.path.join(project_path,'report','test_report'+t+'.html')
report_path = os.path.join(project_path,"report",'report.html')
#配置文件路径
if not os.path.exists(project_path + r'\config'):
    os.mkdir(project_path + r'\config')
config_path = os.path.join(project_path,'config','http_case.config')
