#coding=utf-8
#__author__ = 'xuguoliang'
#description='''  '''

import os
import sys
import hashlib
from get_parent_dir import get_parent_dir
this_package_path = get_parent_dir()
Moudules_path = get_parent_dir(this_package_path)
sys.path.append(Moudules_path)