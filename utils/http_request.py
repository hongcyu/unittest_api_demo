# -*-coding: utf8 -*-

'''
file name:http_request.py
判断request请求是否为get请求，返回请求的结果

'''

import requests

class Http_request(object):
    @staticmethod
    def http_request(url,data,method,excepted=None,cookie=None):
        if method.lower() == 'get':
            res = requests.get(url,data = None,cookies = cookie,verify = False)
            #verify忽略ssl证书警告
        else:
            res = requests.post(url,data,cookies = cookie,verify=False)

        return res


