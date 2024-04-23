from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import HtmlTestRunner


class onboardWorker(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("case started")

    def test_worker(self):
        try:
            self.driver.get("https://www.qa-eflex.okaygo.in/")
            self.driver_wait = WebDriverWait(self.driver, 10)
            email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
            email_input.send_keys("himanshu007")
            password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
            password_input.send_keys("Himanshu@123")
            login_button = self.driver_wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "Login_loginButton__14J9m")))
            login_button.click()

        except Exception as e:
            print(f"Exception occurred: {e}")

    def test_upload(self):
        try:
            self.driver.get("https://www.qa-eflex.okaygo.in/")
            self.driver_wait = WebDriverWait(self.driver, 10)
            action = self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="actions"]')))
            action.click()

            worker = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')))
            worker.click()

            select_radio = self.driver_wait.until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[1]/label[2]/span[1]/span[1]')))
            select_radio.click()

            browse = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/label/input')))
            browse.click()
            file_path = "D:/projects/OGEzedox/non-lmd_onboarding_tempate (4).xlsx"
            browse.send_keys(file_path)

            upload = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]')))
            upload.click()

        except Exception as e:
            print(f"Exception occurred: {e}")


    @classmethod
    def tearDownClass(cls):
        try:
            time.sleep(2)
            cls.driver.close()
            cls.driver.quit()
            print("test completed")
        except WebDriverException as e:
            print(f"WebDriverException occurred during tearDown: {e}")
        except Exception as e:
            print(f"Exception occurred during tearDown: {e}")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/projects/OkayGo/Reports'))
