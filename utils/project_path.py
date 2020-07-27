# -*-coding: utf8 -*-

'''
project_path.py
实现路径的可配置，避免使用相对路径，防止出错

'''
import os

path =os.path.split(os.path.split(os.path.realpath(__file__))[0])
