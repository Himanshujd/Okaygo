from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup driver (Chrome in this case)
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# Step 1: Go to URL
driver.get("https://uat.okaygoprod.in/org/process_okaygo")

# Step 2: Login
username = wait.until(EC.presence_of_element_located((By.ID, "Email")))  # adjust locator
password = driver.find_element(By.ID, "Password")  # adjust locator
login_btn = driver.find_element(By.CLASS_NAME, "login_btn")  # adjust locator

username.send_keys("himanshu.tiwari@mails.okaygo.in")
password.send_keys("OkayGo@123")
login_btn.click()


# Change project - wait for loader to disappear
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "busy_loader")))
dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdownMenuButton")))
driver.execute_script("arguments[0].click();", dropdown)
time.sleep(2)  # Wait for dropdown to open

# Debug: Print available options
options = driver.find_elements(By.XPATH, "//div[@class='dropdown-menu show']//div | //div[contains(@class, 'dropdown-item')]")
print(f"Available options: {[opt.text for opt in options]}")

# Step 3: Go to Jubilant Food Works project
# Scroll within dropdown menu
dropdown_menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dropdown-menu")))
driver.execute_script("arguments[0].scrollTop = 400;", dropdown_menu)

jubilant_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Jubilant Food Works']")))
driver.execute_script("arguments[0].click();", jubilant_option)

# Step 4: Click on Add Tasks
# Debug: Print available buttons
buttons = driver.find_elements(By.TAG_NAME, "button")
print(f"Available buttons: {[btn.text.strip() for btn in buttons if btn.text.strip()]}")

# Try multiple selectors for Add Tasks
try:
    add_task_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='right_side']/main/div[1]/div[2]/button[3]")))
except:
    add_task_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='right_side'']/main/div[1]/div[2]/button[3]")))
driver.execute_script("arguments[0].click();", add_task_btn)

# Step 5: Browse file to upload
file_path = "/Users/himanshu.tiwari/Okaygo/bulk_sample (4).xlsx"
print(f"Attempting to upload file: {file_path}")

# Click BROWSE FILE area
# browse_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/section/div/p/span")))
# browse_btn.click()

file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys(file_path)

# Step 6: Click on Upload
original_tab = driver.current_window_handle
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button"))).click()

# Wait and switch back to original tab
time.sleep(2)
driver.switch_to.window(original_tab)

open_bucket= wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='right_side']/main/div[2]/div/div/ul/li[2]/a")))
open_bucket.click()

select_task = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='open_process']/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input")))
select_task.click()


action = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='actions']")))
action.click()

assign = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='menu-']/div[3]/ul/li[2]")))
assign.click()


# Step 7: Assign task to worker by searching email ID
# Debug: Print available inputs
inputs = driver.find_elements(By.TAG_NAME, "input")
print(f"Available inputs: {[inp.get_attribute('placeholder') for inp in inputs]}")

# Try multiple selectors for search box
try:
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/div/div[1]/span/span/span[2]/input")))
except:
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/div/div[1]/span/span/span[2]/input")))

search_box.send_keys("himanshu.tiwari@mails.okaygo.in")
time.sleep(2)
search_box.send_keys(Keys.RETURN)

wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/input"))).click()


# Step 8: Select worker and click Assign
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div[2]/button[2]"))).click()

# Step 9: Go to Assigned Bucket
# Wait for any loader to disappear first
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "busy_loader")))
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='right_side']/main/div[2]/div/div/ul/li[4]/a"))).click()

# Step 10: Click on Action to start form
# Scroll horizontally to make button visible
driver.execute_script("document.querySelector('#assigned_process').scrollLeft = 500;")
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='assigned_process']/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[12]/button[1]"))).click()

# Step 11: Fill form.io form
time.sleep(5)  # Wait for form to load

# Function to scroll to element and interact
def scroll_and_interact(locator, action_type="click", value=None):
    element = wait.until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(0.5)
    if action_type == "click":
        element.click()
    elif action_type == "send_keys" and value:
        element.send_keys(value)
    return element

# Example usage for form fields
# scroll_and_interact((By.ID, "field_id"), "send_keys", "your_value")
# scroll_and_interact((By.XPATH, "//button[text()='Submit']"), "click")

print("Process completed!")

time.sleep(2)
driver.quit()
