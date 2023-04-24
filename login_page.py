from selenium import webdriver
import unittest
import time


class LoginAdminDashboard(unittest.TestCase):
    print("case started")

    @classmethod
    def setupBrowser(bro):
        bro.driver = webdriver.Chrome(executable_path='..\Driver\chromedriver.exe')
        bro.driver.implicitly_wait(30)
        bro.driver.maximize_window()

        print("successfully opened")

    def loginCredentials(log):
        log.driver.get("https://www.qa-eflex.okaygo.in/")
        log.driver.find_element_by_id("emailId").send_keys("himanshu007")
        log.driver.find_element_by_id("password").send_keys("Himanshu@123")
        log.driver.find_element_by_class("Login_loginButton__14J9m").send_keys("Login")

    @classmethod
    def closeBrowser(bro):
        bro.time.sleep(3)
        bro.driver.close()

        print("successfully logedin")