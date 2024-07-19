import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class testAddJob(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test suite started")

    def setUp(self):
        self.driver.get("https://www.qa-eflex.okaygo.in/jobsdb")
        self.driver_wait = WebDriverWait(self.driver, 10)

    def test_add_job(self):
        try:
            self.login()
            self.addJob()
        except Exception as e:
            print(f"Exception occurred: {e}")

    def login(self):
        email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
        email_input.send_keys("himanshu007")
        password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_input.send_keys("Himanshu@123")
        login_button = self.driver_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
        login_button.click()

    def addJob(self):
        try:
            add_job_button = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[3]/div/div[1]/div[2]/a/button")))
            add_job_button.click()

            select_project_name = self.driver_wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='projectName']")))
            select_project_name.send_keys("surbhi test")

        except TimeoutException:
            print("Element not found or not clickable")

        enter_job_title = self.driver_wait.until(
            EC.element_to_be_clickable(By.XPATH, "//*[@id='outlined-adornment-weight']"))
        enter_job_title.send_keys("job")


# select_vertical_name = self.driver_wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[6]/div/label[1]/span[1]')))
# select_vertical_name.click()
#
# select_project_owner_name = self.driver_wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[6]/div/label[1]/span[1]')))
# select_project_owner_name.click()
#
# enter_description = self.driver_wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[6]/div/label[1]/span[1]')))
# enter_description.send_keys()
#
# enter_project_key = self.driver_wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[6]/div/label[1]/span[1]')))
# random_name = self.generate_random_name()
# enter_project_key.send_keys(random_name)
#
# submit = self.driver_wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[2]/div[10]/div/button')))
# submit.click()

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
