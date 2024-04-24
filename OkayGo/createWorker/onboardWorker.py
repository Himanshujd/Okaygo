import traceback
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOnboardWorker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test suite started")

    def setUp(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/")
        self.driver_wait = WebDriverWait(self.driver, 10)

    def test_upload_worker_data(self):
        try:
            self.login()
            self.navigate_to_worker_section()
            self.select_worker_type("Non-LMD")
            self.upload_file()
            # print("File uploaded successfully")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def login(self):
        email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu007")
        password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@123")
        login_button = self.driver_wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()

    def navigate_to_worker_section(self):
        action = self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="actions"]')))
        action.click()
        worker = self.driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')))
        worker.click()

    def select_worker_type(self, worker_type):
        select_radio = self.driver_wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[1]/label[2]/span[1]/span[1]')))
        select_radio.click()

    def upload_file(self):
        try:
            file_path = "D:/projects/OkayGo/createWorker/non-lmd_onboarding_tempate (4).xlsx"
            print(f"Attempting to upload file: {file_path}")

            # # Wait for the browse button to be clickable
            # browse = self.driver_wait.until(
            #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Browse File')]")))
            # browse.click()

            # Wait for the file input to be present
            file_input = self.driver_wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

            # Send the file path to the file input
            file_input.send_keys(file_path)

            # Wait for the file to be uploaded
            print("Upload in process")
            upload_button = self.driver_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[2]/div[3]/div/div[3]/button")))
            upload_button.click()

            print("File uploaded successfully")

        except ElementNotInteractableException:
            print("File input element is not interactable. Make sure it's visible and enabled.")

        except Exception as e:
            print(f"Exception occurred while uploading file: {e}")
            print(traceback.format_exc())
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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D://projects/OkayGo/Reports'))
