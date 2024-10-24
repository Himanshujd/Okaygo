import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import HtmlTestRunner

class LoginAdminDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver_wait = WebDriverWait(cls.driver, 10)
        cls.login_successful = False

    def login(self, username, password):
        self.driver.get("https://www.qa-eflex.okaygo.in/")
        try:
            email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
            email_input.send_keys(username)
            password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
            password_input.send_keys(password)
            login_button = self.driver_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
            login_button.click()
        except TimeoutException:
            self.fail("Login elements were not found in the expected time frame")

    def logout(self):
        try:
            logout_button = self.driver_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/div/div[2]/header/div/button[2]/span[1]")))
            logout_button.click()
        except TimeoutException:
            self.fail("Logout button not found or not clickable")

    def tearDown(self):
        """Logout only if login was successful"""
        if self.login_successful:
            try:
                self.logout()
            except Exception as e:
                print(f"Error during logout: {e}")

    # First test case: correct username and password
    def test_01_login_valid(self):
        """Test with correct username and password"""
        self.login("himanshu007", "Himanshu@123")
        try:
            dashboard_element = self.driver_wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "Header_logout__WB1NW")))
            self.assertTrue(dashboard_element.is_displayed(), "Login failed, dashboard not visible.")
            print('First case - Correct username and password')
            self.login_successful = True  # Mark the login as successful
        except TimeoutException:
            self.fail("Dashboard not found after successful login")

    # Second test case: incorrect username
    def test_02_login_invalid_username(self):
        """Test with incorrect username"""
        self.login("himanshu0", "Himanshu@123")
        try:
            error_message = self.driver_wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
            self.assertTrue(error_message.is_displayed(), "Error message not displayed.")
            print('Second case - Incorrect username')
        except TimeoutException:
            self.fail("Error message not found for incorrect username")

    # Third test case: incorrect password
    def test_03_login_invalid_password(self):
        """Test with incorrect password"""
        self.login("himanshu007", "Himanshu@")
        try:
            error_message = self.driver_wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
            self.assertTrue(error_message.is_displayed(), "Error message not displayed.")
            print('Third case - Incorrect password')
        except TimeoutException:
            self.fail("Error message not found for incorrect password")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("All tests completed")


if __name__ == '__main__':
    output_dir = '/Users/himanshu.tiwari/Okaygo/OkayGo/reports'
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=output_dir, report_title='Login Tests Report', descriptions='Test Results for Login Module'))