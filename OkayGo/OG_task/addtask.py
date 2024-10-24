import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import USERNAME, PASSWORD, URL


class AddTask(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(URL)

    def test_add_task(self):
        try:
            # Wait for login elements to load
            username_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='Email']"))
            )
            username_input.send_keys(USERNAME)

            password_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@id='Password']"))
            )
            password_input.send_keys(PASSWORD)

            login_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@class='login_btn']"))
            )
            login_button.click()

            # Wait for the "busy_loader" overlay to disappear
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "busy_loader"))
            )

            # Wait for project dropdown to load
            project_dropdown = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='dropdownMenuButton']/span")))
            project_dropdown.send_keys("Betterplace Field Verification Non Metro", Keys.RETURN)

            # Wait for "Add Task" button to load
            add_task_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='right_side']/main/div/div[2]/button[3]")))
            add_task_button.click()

            file_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
            file_path = "D://projects/OGEzedox/Resources/samplemportfileforBGV.xlsx"
            file_input.send_keys(file_path)

            upload_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button")))
            upload_button.click()

        except TimeoutException as te:
            print("Timeout occurred while waiting for element:", te)
        except Exception as e:
            print("An error occurred:", e)

    @classmethod
    def tearDownClass(cls):
        # Close the browser window
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
