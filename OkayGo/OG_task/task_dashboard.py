import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
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
                EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section/section[2]/section/div[2]/input"))
            )
            enter_mobile.send_keys(mobile_number)
            login_button = self.driver_wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/section/div")))
            login_button.click()
        except TimeoutException:
            self.fail("Login elements were not found in the expected time frame")

    def logout(self):
        try:
            menu = self.driver_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/section[1]/section/div/div[1]/div[1]"))
            )
            menu.click()

            logout_button = self.driver_wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/section[1]/section/section[5]/div/div[2]"))
            )
            logout_button.click()
        except TimeoutException:
            self.fail("Logout button not found or not clickable")

    def test_start_task(self):
        try:
            self.login("8755043788")

            # Wait for the project dropdown to be clickable
            project_dropdown = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/section[2]/div[1]/div/div[1]"))
            )
            project_dropdown.click()

            # Wait for all project options to be visible
            project_options = self.driver_wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='root']/section[2]/div[1]/div/div[3]/div[8]"))
            )

            # Click the desired option
            if project_options:
                ActionChains(self.driver).move_to_element(project_options[0]).click().perform()

            # Now locate and click the task button
            task_button = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/section[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/a"))
            )
            task_button.click()

           # Wait for the form page to load
            self.driver_wait.until(EC.url_changes("https://task.okaygo.in/task-page/"))

            # Define form_data for the form fields on the page
            form_data = [
                {
                    'type': 'text',
                    'locator': (By.XPATH, "//input[@placeholder='Your Name']"),
                    'value': 'John Doe'
                },
                {
                    'type': 'dropdown',
                    'locator': (By.XPATH, "//input[@placeholder='Select Status']"),
                    'value': 'active'
                },
                {
                    'type': 'file',
                    'locator': (By.XPATH, "//input[@type='file']"),
                    'value': '/Users/himanshu.tiwari/Okaygo/OkayGo/OG_task/download (5).png'
                },
                {
                    'type': 'text',
                    'locator': (By.XPATH, "//input[@placeholder='Date']"),
                    'value': '2024-11-11'
                }
            ]

            # Call fill_form with the form_data
            self.fill_form(form_data)

        except Exception as e:
            print(f"An error occurred in test_start_task: {e}")

    def fill_form(self, form_data):
        """
        Fills a form based on the given form_data dictionary.
        """
        for field in form_data:
            field_type = field.get('type')
            locator = field.get('locator')
            value = field.get('value')

            try:
                # Scroll to the element before interacting with it
                element = self.driver_wait.until(EC.visibility_of_element_located(locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

                if field_type == 'text':
                    element.clear()
                    element.send_keys(value)

                elif field_type == 'dropdown':
                    element.click()
                    option = self.driver_wait.until(
                        EC.element_to_be_clickable((By.XPATH, f"//*[text()='{value}']")))
                    option.click()

                elif field_type == 'file':
                    element.send_keys(value)

                else:
                    print(f"Unknown field type: {field_type}")

                time.sleep(0.5)

            except Exception as e:
                print(f"Error processing field {field}: {e}")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print("All tests completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/himanshu.tiwari/Okaygo/OkayGo/reports'))
