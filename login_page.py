from selenium import webdriver
import unittest

class LoginAdminDashboard(unittest.TestCase):

    @classmethod
    def openBrowser(bro):
        bro.driver =webdriver.Chrome(executable_path='../driver/chromedriver.exe')
        bro.driver.implicitly_wait(10)
        bro.driver.maximize_window()
        bro.driver.get("https://www.qa-eflex.okaygo.in/")  
        print("successfully opened")

         