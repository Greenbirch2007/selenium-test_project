# -*- coding:utf-8 -*-
import unittest
import datetime
# 用sys.path.insert(0,"目录的路径") 暴力添加路径
from test_case import sougou
from test_case import baidu


suite = unittest.TestSuite()

suite.addTest(baidu.Testbaidu("test_baidu"))

suite.addTest(sougou.Testsougou("test_sougou"))   # suite.addTest(模块名.类名.("函数名"))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)

print("Test_case's bingo time",datetime.datetime.now())

    

