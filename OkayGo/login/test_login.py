import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner


class LoginAdminDashboard(unittest.TestCase):
    print('Automation testing started')

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # first test case if user entered the correct user_name and password
    def test_login1(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/")
        self.driver_wait = WebDriverWait(self.driver, 10)
        email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu007")
        password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@123")
        login_button = self.driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()
        print('First case- correct username and password')

    # second test case if user entered the Incorrect user_name
    def test_login2(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/")
        self.driver_wait = WebDriverWait(self.driver, 10)
        email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu0")
        password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@123")
        login_button = self.driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()
        print('Second case- Incorrect username')

    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
    # Third test case if user entered the Incorrect user_name
    def test_login3(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/")
        self.driver_wait = WebDriverWait(self.driver, 10)
        email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu007")
        password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@")
        login_button = self.driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()
        print('Third case- Incorrect password')

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/himan/PycharmProjects/Okaygo1/reports'))