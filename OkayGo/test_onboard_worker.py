# test_onboard_worker.py
import time
import traceback
import unittest

import HtmlTestRunner
from parameterized import parameterized
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_test import BaseTest


class TestOnboardWorker(BaseTest):

    @parameterized.expand([
        ("D:/projects/OkayGo/createWorker/non-lmd_onboarding_template (4).xlsx",),

    ])
    def test_upload_worker_data(self, file_path):
        try:
            self.navigate_to_worker_section()
            self.select_worker_type()
            self.upload_file(file_path)
        except Exception as e:
            print(f"Exception occurred: {e}")

    def navigate_to_worker_section(self):
        action = self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="actions"]')))
        action.click()
        worker = self.driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')))
        worker.click()

    def select_worker_type(self):
        select_radio = self.driver_wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[1]/label[2]/span[1]/span[1]')))
        select_radio.click()

    def upload_file(self, file_path):
        try:
            print(f"Attempting to upload file: {file_path}")

            file_input = self.driver_wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
            file_input.send_keys(file_path)

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


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\projects\\OkayGo\\Reports'))
