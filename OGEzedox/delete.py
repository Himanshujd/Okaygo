from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeleteAutomation:
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def automate_deletion(self):
        try:
            self.driver.get("https://uat.okaygoprod.in/api/admin/user/user/")
            self.driver_wait = WebDriverWait(self.driver, 10)
            email_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "id_username")))
            email_input.send_keys("vishal@uat.com")  # Change the email for login
            password_input = self.driver_wait.until(EC.visibility_of_element_located((By.ID, "id_password")))
            password_input.send_keys("123456789")
            login_button = self.driver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "submit-row")))
            login_button.click()

            while True:
                # Wait for the checkboxes to load
                checkboxes = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="checkbox"][name="_selected_action"]'))
                )

                # If there are no checkboxes, break out of the loop
                if not checkboxes:
                    print("No items left to delete.")
                    break

                # First, select all checkboxes
                for checkbox in checkboxes:
                    checkbox.click()

                # Then, find and unselect the checkbox identified by the XPath
                specific_checkbox = self.driver.find_element(By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/td[@class="action-checkbox"]/input')
                specific_checkbox.click()

                # Find the "With selected" dropdown
                with_selected_dropdown = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.NAME, "action"))
                )

                # Select the option "Delete selected Users"
                for option in with_selected_dropdown.find_elements(By.TAG_NAME, 'option'):
                    if option.text == 'Delete selected Users':
                        option.click()
                        break

                # Find the "Go" button and click it
                go_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="changelist-form"]/div[1]/button'))
                )
                go_button.click()

                # Find and click the confirmation button
                confirmation_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//input[@value="Yes, I’m sure"]'))
                )
                confirmation_button.click()

                print("Deletion process completed successfully.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")


# Instantiate the class and call the function to start the automation process
delete_automation = DeleteAutomation()
delete_automation.setUpClass()
delete_automation.automate_deletion()
delete_automation.tearDownClass()
