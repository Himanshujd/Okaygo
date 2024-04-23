import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import login_test
import time

class addMPA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
def test_addMpa(self):
    login = login_test.LoginAdminDashboard(self.driver)

    self.driver_wait = WebDriverWait(self.driver, 10)
    add_mpa_button = self.driver_wait.until (EC.visibility_of_element_located((By.CLASS_NAME, "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-4")))
    add_mpa_button.click()
    # password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "password")))
    # password_input.send_keys("Himanshu@123"
    # login_button = self.driver_wait.until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "Login_loginButton__14J9m")))
    # login_button.click()

@classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()