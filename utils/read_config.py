# -*-coding: utf8 -*-

'''
read_config.py
用于读取config文件的方法

'''

import configparser
import init_path

class Read_config(object):

    @staticmethod
    def get_config(config_path,section,option):
        config = configparser.ConfigParser() #初始化对象
        config.read(config_path,encoding="utf-8")#注意使用utf-8编码读取
        return config[section][option]

if __name__ == "__main__":
    pass
    # cf = Read_config.get_config(init_path.config_path,'MODE','mode')
    # print(cf)
    
    