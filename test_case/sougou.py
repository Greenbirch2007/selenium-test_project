#! -*- coding:utf-8 -*-

from selenium import webdriver
import unittest
import time
import datetime



class Testsougou(unittest.TestCase):

    def setUp(self):
        start = datetime.datetime.now()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.sogou.com/"
        print("sougou start!",start)

    def test_sougou(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id('query').send_keys('webdriver')
        driver.find_element_by_id('stb').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,"webdriver - 搜狗搜索")

    def tearDown(self):
        self.driver.close()
        end = datetime.datetime.now()
        print("sougou ok!",end)

if __name__ == "__main__":
    unittest.main()

