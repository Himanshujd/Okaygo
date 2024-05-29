import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class TestAddEmployer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test suite started")

    def setUp(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/employer-data")
        self.driver_wait = WebDriverWait(self.driver, 10)

    def test_add_employer_data(self):
        try:
            self.login()
            self.addEmployer()
        except Exception as e:
            print(f"Exception occurred: {e}")

    def login(self):
        email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu007")
        password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@123")
        login_button = self.driver_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()

    def generate_random_name(self, length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def addEmployer(self):
        try:
            add_employer = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/a/button'))
            )
            add_employer.click()

            enter_client_name = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="outlined-basic"]'))
            )
            random_name = self.generate_random_name()
            enter_client_name.send_keys(random_name)

        except TimeoutException:
            print("Element not found or not clickable")

        file_path = "D:/projects/OkayGo/createEditEmployer/download (5).png"
        print(f"Attempting to upload file: {file_path}")

        # Locate the file input element and send the file path to it
        upload_client_logo = self.driver_wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="contained-button-file"]')))
        upload_client_logo.send_keys(file_path)

        document_required_checkbox = self.driver_wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[6]/div/label[1]/span[1]')))
        document_required_checkbox.click()

        submit = self.driver_wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[10]/div/button')))
        submit.click()

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\projects\\OkayGo\\Reports'))
