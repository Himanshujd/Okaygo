
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class testAddProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("Test suite started")

    def setUp(self):
        self.driver.get("https://qa.okaygo.in/mark-attendance/0Oc5uCkUIPYwQmnScsVn%2Fg%3D%3D")
        self.driver_wait = WebDriverWait(self.driver, 10)

    def test_markAttendance(self):
        try:
            self.attendance()

        except Exception as e:
            print(f"Exception occurred: {e}")

    def attendance(self):
        click_selfie = self.driver_wait.until(EC.visibility_of_element_located(By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[4]/button"))
        click_selfie.click()
        take_selfie = self.driver_wait_until(EC.visibility_of_element_located(By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[5]/div/div/button[1]"))
        take_selfie.click()
        enter_phone_number = self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[5]/div/div/input")))
        enter_phone_number.send_keys("9389512958")
        click_verify = self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[5]/div/div/div")))
        click_verify.click()
        # login_button = self.driver_wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
        # login_button.click()

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