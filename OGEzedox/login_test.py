from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class LoginAdminDashboard(unittest.TestCase):
    driver = None  # Class variable to store the WebDriver instance

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/")
        self.driver_wait = WebDriverWait(self.driver, 10)
        email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu007")
        password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@123")
        login_button = self.driver_wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
