# -*-coding: utf8 -*-


import sys
import os
sys.path.append(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])

import unittest
from ddt import ddt,data
from utils import project_path
from utils import read_excel
from units import read_config

print(project_path.config_path)