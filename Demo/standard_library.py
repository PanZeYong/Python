#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 10.Python 标准库概览

# 操作系统接口模块：os
# 文件目录管理模块：shutil
# 文件工具：glob
# 字符串处理：re
# 数学操作：math
# 随机数：random
# 网络请求模块：request
# 日期和时间：datetime
# 数据压缩：zlib，gzip，bz2，lzma，zipfile，tarfile
# 性能度量：timeit
# 时间度量工具：profile 和 pstats
# 质量控制：doctest（扫描模块并根据程序中内嵌的文档字符串执行测试）
import os
import shutil
import glob
import re
import math
import random
import datetime
import zlib
import doctest
import unittest

from urllib.request import urlopen
from datetime import date
from timeit import Timer

class TestStatisticalFunctions(unittest.TestCase):
    
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        # self.assertEqual(round(average([1, 5, 7])), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """

    return sum(values) / len(values)

if __name__ == '__main__':
    print(os.getcwd())    # Return the current working directory
    os.chdir('/Users/Pan/Language/Python')
    # re 模块
    print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
    print('tea for too'.replace('too', 'two'))

    # math 模块
    print(math.cos(math.pi / 4.0))
    print(math.log(1024, 2))

    # random 模块
    print(random.choice(['apple', 'pear', 'banana']))
    print(random.sample(range(100), 10))    # sampling without replacement
    print(random.random())    # random float
    print(random.randrange(6))    # random integer chosen from range(6)

    # request 模块
    # for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    #     line = line.decode('utf-8')    # Decoding the binary data to text
    #     if 'EST' in line or 'EDT' in line:    # look for Eastern Time
    #         print(line)

    # datetime 日期和时间
    # dates are easily constructed and formatted
    now = date.today()
    print(now)
    print(datetime.date(2013, 12, 3))
    print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
    # dates support calendar arithmetic
    birthday = date(1964, 7, 31)
    age = now - birthday
    print(age.days)

    # 数据压缩：zlib，gzip，bz2，lzma，zipfile，tarfile
    s = b'witch which has which witches wrist watch'
    print(len(s))
    t = zlib.compress(s)
    print(len(t))
    print(zlib.decompress(t))
    print(zlib.crc32(s))

    # 性能度量：timeit
    print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
    print(Timer('a,b = b,a', 'a=1; b=2').timeit())

    # 质量控制：doctest
    doctest.testmod()    # automatically validate the embedded tests
    unittest.main()
    # os.system('mkdir test')
    # dir(os)
    # help(os)
    # dir(glob)
    # help(glob)
    # print(glob.glob('/Users/Pan/Language/Python/Demo/*.py', recursive=True))
    