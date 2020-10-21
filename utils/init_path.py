
import os
#####################路径自定义#####################
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
test_case_path = os.path.join(project_path,'data','data_http.xlsx')
report_path = os.path.join(project_path,"report",'report.html')
config_path = os.path.join(project_path,'config','http_case.config')
#####################路径自定义#####################