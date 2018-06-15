#! -*- coding:utf-8 -*-

from selenium import webdriver
import unittest
import time
import datetime



class Testbaidu(unittest.TestCase):
    def setUp(self):
        start = datetime.datetime.now()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
        print("baidu start!",start)

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys("unittest")
        driver.find_element_by_id('su').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,"unittest_百度搜索")
                

    def tearDown(self):
        self.driver.quit()
        end = datetime.datetime.now()
        print("baidu ok!",end)
        

if __name__ == "__main__":
    unittest.main()



