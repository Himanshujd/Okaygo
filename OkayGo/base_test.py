# base_test.py
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from login_helper import login


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test suite started")

    def setUp(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/")
        self.driver_wait = WebDriverWait(self.driver, 10)
        login("himanshu007", "Himanshu@123")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test suite completed")
