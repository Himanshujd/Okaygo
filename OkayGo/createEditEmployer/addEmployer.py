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
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver_wait = WebDriverWait(cls.driver, 10)

    def login(self, username, password):
        self.driver.get("https://www.qa-eflex.okaygo.in/employer-data")
        try:
            email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
            email_input.send_keys(username)
            password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
            password_input.send_keys(password)
            login_button = self.driver_wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
            login_button.click()
        except TimeoutException:
            self.fail("Login elements were not found in the expected time frame")

    def test_add_multiple_employers(self):
        """Test adding multiple employers in a loop"""
        self.login("himanshu007", "Himanshu@123")
        num_employers_to_add = 1  # Set the number of employers you want to add
        for i in range(num_employers_to_add):
            print(f"Adding employer {i + 1} of {num_employers_to_add}")
            try:
                self.addEmployer(i + 1)  # Pass the count to the addEmployer function to identify each employer
            except Exception as e:
                self.take_screenshot(f"add_employer_error_{i + 1}.png")
                print(f"Exception occurred while adding employer {i + 1}: {e}")

    def generate_random_name(self, length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def addEmployer(self, employer_number):
        try:
            # Click 'Add Employer' button
            add_employer = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/a/button'))
            )
            add_employer.click()

            # Enter random client name
            enter_client_name = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="outlined-basic"]'))
            )
            random_name = f"{self.generate_random_name()}_{employer_number}"
            enter_client_name.send_keys(random_name)

            # Verify client name input
            self.assertEqual(enter_client_name.get_attribute('value'), random_name,
                             "Client name is not correctly entered.")

            # Upload a logo for the employer
            file_path = "/Users/himanshu.tiwari/Okaygo/OkayGo/createEditEmployer/download (5).png"
            # print(f"Attempting to upload file for employer {employer_number}: {file_path}")
            upload_client_logo = self.driver_wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="contained-button-file"]')))
            upload_client_logo.send_keys(file_path)

            # Check a checkbox for document requirement
            document_required_checkbox = self.driver_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[6]/div/label[1]/span[1]')))
            document_required_checkbox.click()

            # Submit the form
            submit = self.driver_wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[10]/div/button')))
            submit.click()

            # Verify success message
            try:
                success_message = self.driver_wait.until(
                    EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]'))
                )
                self.assertTrue(success_message.is_displayed(),
                                f"Success message not displayed for employer {employer_number}.")

                # Close the success message pop-up
                close_popup = self.driver_wait.until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/div/button')))
                close_popup.click()

            except TimeoutException:
                self.take_screenshot(f"submission_timeout_error_{employer_number}.png")
                self.fail(f"Submission success message not found for employer {employer_number}.")

        except TimeoutException:
            self.take_screenshot(f"element_timeout_error_{employer_number}.png")
            print(f"Element not found or not clickable for employer {employer_number}")

def take_screenshot(self, filename):
    """Take a screenshot of the current browser window."""
    self.driver.save_screenshot(filename)
    print(f"Screenshot saved as {filename}")


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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/himanshu.tiwari/Okaygo/OkayGo/reports"))
