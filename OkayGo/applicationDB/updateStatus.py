import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ApplicationDBTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test suite started")

    def setUp(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/applicationDb")
        self.driver_wait = WebDriverWait(self.driver, 10)

    def test_applicationdb(self):
        try:
            self.login()
            self.update_status()
        except Exception as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")

    def login(self):
        try:
            email_input = self.driver_wait.until(
                EC.visibility_of_element_located((By.ID, "emailId")))
            email_input.send_keys("himanshu007")
            password_input = self.driver_wait.until(
                EC.visibility_of_element_located((By.ID, "password")))
            password_input.send_keys("Himanshu@123")
            login_button = self.driver_wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
            login_button.click()
        except TimeoutException as e:
            print(f"TimeoutException in login: {e}")
            self.driver.save_screenshot("login_timeout.png")
            raise

    def update_status(self):
        try:
            open_job_list = self.driver_wait.until(
                EC.visibility_of_element_located((By.ID, "search-select")))
            open_job_list.click()
            select_job = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='menu-']/div[3]/ul/li[7]")))
            select_job.click()
            applied_bucket = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='simple-tab-1']/span[1]")))
            applied_bucket.click()
            select_worker = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div[3]/div/div[4]/div[1]/table/thead/tr/th[1]")))
            select_worker.click()
            dropdown = self.driver_wait.until(
                EC.visibility_of_element_located((By.ID, "//*[@id='root']/div/div[3]/div/div[4]/div[1]/table/thead/tr/th[1]")))
            dropdown.click()
            option = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div[3]/div/div[4]/div[1]/table/thead/tr/th[1]")))
            option.click()

        except TimeoutException as e:
            print(f"TimeoutException in update_status: {e}")
            self.driver.save_screenshot("update_status_timeout.png")
            raise

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.close()
            cls.driver.quit()
            print("Test suite completed")
        except WebDriverException as e:
            print(f"WebDriverException occurred during tearDown: {e}")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/himanshu.tiwari/Okaygo/Okaygo/reports'))
