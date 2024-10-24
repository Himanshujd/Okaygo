import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import HtmlTestRunner

class taskDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver_wait = WebDriverWait(cls.driver, 10)
        cls.login_successful = False

    def login(self, mobile_number):
        self.driver.get("https://task.okaygo.in/")
        try:
            enter_mobile = self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section/section[2]/section/div[2]/input")))
            enter_mobile.send_keys(mobile_number)
            # password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
            # password_input.send_keys(password)
            login_button = self.driver_wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/section/div")))
            login_button.click()
        except TimeoutException:
            self.fail("Login elements were not found in the expected time frame")

    def logout(self):
        try:
            menu = self.driver_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/section[1]/section/div/div[1]/div[1]")))
            menu.click()

            logout_button = self.driver_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/section[1]/section/section[5]/div/div[2]")))
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

    # First test case: correct mobile number
    def test_01_login_valid(self):
        """Test with correct mobile number"""
        self.login("8755043788")
        try:
            dashboard_element = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section/div")))
            self.assertTrue(dashboard_element.is_displayed(), "Login failed, dashboard not visible.")
            print('First case - Worker Mobile Number')
            self.login_successful = True  # Mark the login as successful
        except TimeoutException:
            self.fail("Dashboard not found after successful login")

    # Second test case: incorrect username
    def test_02_login_invalid_mobilenumber(self):
            """Test with incorrect username"""
            self.login("87550437")
            try:
                error_message = self.driver_wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section/section[2]/div/div/div[2]")))
                self.assertTrue(error_message.is_displayed(), "Error message not displayed.")
                print('Second case - Incorrect Mobile Number')
            except TimeoutException:
                self.fail("Error message not found for Incorrect Mobile Number")

    # Third test case: incorrect password
    def test_03_login_lead_mobilenumber(self):
            """Test with incorrect password"""
            self.login("8755000788")
            try:
                error_message = self.driver_wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section/section[2]/div/div/div[2]")))
                self.assertTrue(error_message.is_displayed(), "Error message not displayed.")
                print('Third case - Lead Mobile Number')
            except TimeoutException:
                self.fail("Error message not found for Lead Mobile Number ")


    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("All tests completed")

if __name__ == '__main__':
    output_dir = '/Users/himanshu.tiwari/Okaygo/OkayGo/reports'
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=output_dir, report_title='Login Tests Report', descriptions='Test Results for Login Module'))
