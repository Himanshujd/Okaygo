from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class DeleteAutomation:
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


driver.get("https://form.io/#/forms")

# Wait for the page to load
time.sleep(5)

# Define function to drag and drop elements
def drag_and_drop(source, target):
    ActionChains(driver).drag_and_drop(source, target).perform()
    time.sleep(1)

try:
    # Find the "Basic Components" section
    basic_components_section = driver.find_element(By.XPATH, "//div[contains(text(),'Basic Components')]")

    # Find the first component, for instance, "Text Field"
    text_field = driver.find_element(By.XPATH, "//div[contains(text(),'Text Field')]")

    # Find the form canvas where we want to drop the components
    form_canvas = driver.find_element(By.CLASS_NAME, "formbuilder-drop-zone")

    # Drag and drop the text field to the form canvas
    drag_and_drop(text_field, form_canvas)

    # You can repeat the process for other components if needed

    # Example: Dragging a Text Area component
    text_area = driver.find_element(By.XPATH, "//div[contains(text(),'Text Area')]")
    drag_and_drop(text_area, form_canvas)

    # Example: Dragging a Date component
    date_field = driver.find_element(By.XPATH, "//div[contains(text(),'Date')]")
    drag_and_drop(date_field, form_canvas)

    # Example: Dragging a Dropdown component
    dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'Dropdown')]")
    drag_and_drop(dropdown, form_canvas)

    # Example: Dragging a Checkboxes component
    checkboxes = driver.find_element(By.XPATH, "//div[contains(text(),'Checkboxes')]")
    drag_and_drop(checkboxes, form_canvas)

    # You can add more components as needed

    # Once components are added, save the form
    save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
    save_button.click()

    # Wait for the form to be saved
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser window
    driver.quit()
