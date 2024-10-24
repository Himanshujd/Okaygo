import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TaskDashboard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver_wait = WebDriverWait(cls.driver, 10)

    def login(self, mobile_number):
        self.driver.get("https://task.okaygo.in/")
        try:
            enter_mobile = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section/section[2]/section/div[2]/input")))
            enter_mobile.send_keys(mobile_number)
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

    def test_start_task(self):
        try:
            self.login("8755043788")

            # Wait for the project dropdown to be visible
            project_dropdown = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section[2]/div[1]/div/div[1]")))
            project_dropdown.click()

            project_options = self.driver_wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='root']/section[2]/div[1]/div/div[3]/div[8]"))
            )
            project_options.click()

        except Exception as e:
            print(f"An error occurred in test_start_task: {e}")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("All tests completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/himanshu.tiwari/Okaygo/OkayGo/reports'))