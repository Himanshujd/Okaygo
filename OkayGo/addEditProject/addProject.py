import string
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class TestAddProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test suite started")

    def setUp(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/projectConfig")
        self.driver_wait = WebDriverWait(self.driver, 20)

    def test_add_employer_data(self):
        try:
            self.login()
            self.addProject()
        except Exception as e:
            print(f"Exception occurred: {e}")

    def login(self):
        email_input = self.driver_wait.until(
            EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu007")
        password_input = self.driver_wait.until(
            EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@123")
        login_button = self.driver_wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()

    def generate_random_name(self, length=7):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def addProject(self):
        try:
            add_project = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/a/button')))
            add_project.click()

            enter_project_name = self.driver_wait.until(
                EC.visibility_of_element_located((By.ID, 'mui-1"]')))
            random_name = self.generate_random_name()
            enter_project_name.send_keys(random_name)

            client_dropdown_button = self.driver_wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Open']")))
            client_dropdown_button.click()

            # Wait for the dropdown options to appear
            options_container = self.driver_wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']")))

            # Select a random option from the list
            options = options_container.find_elements(By.TAG_NAME, "li")
            random_option = random.choice(options)
            random_option.click()

            vertical_input = self.driver_wait.until(
                EC.visibility_of_element_located((By.ID, "vertical")))
            vertical_input.click()

            options_container = self.driver_wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']")))

            options1 = options_container.find_elements(By.TAG_NAME, "li")
            random_option1 = random.choice(options1)
            random_option1.click()

            project_owner_input = self.driver_wait.until(
                EC.visibility_of_element_located((By.ID, "projectOwner")))
            project_owner_input.click()

            options_container = self.driver_wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']")))

            options2 = options_container.find_elements(By.TAG_NAME, "li")
            random_option2 = random.choice(options2)
            random_option2.click()

            # Scroll to 'Project Key' input and enter a random project key
            project_key_input = self.driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, '')))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", project_key_input)
            random_name1 = self.generate_random_name()
            project_key_input.send_keys(random_name1)

            project_code_input = self.driver_wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '')))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", project_code_input)
            random_name2 = self.generate_random_name()
            project_code_input.send_keys(random_name2)

            submit = self.driver_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[14]/div/button')))
            submit.click()

        except TimeoutException:(
                print("Element not found or not clickable"))


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
