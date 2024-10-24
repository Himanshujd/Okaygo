from selenium import webdriver  # for controlling the browser
from selenium.webdriver.common.keys import Keys  # for using keyboard keys like Enter
import time  # for adding delays

driver = webdriver.Chrome()
driver.get("https://www.qa-eflex.okaygo.in/projectConfig")
time.sleep(2)
email_input = driver.find_element('id', "emailId")
email_input.send_keys("himanshu007")
password_input = driver.find_element("id", "password")
password_input.send_keys("Himanshu@123")
login_button = driver.find_element('class name', "Login_loginButton__14J9m")
login_button.click()

time.sleep(2)

# Take screenshot
driver.save_screenshot("screenshot.png")

driver.get("https://www.qa-eflex.okaygo.in/projectConfig/project/add")
time.sleep(2)
project_field = driver.find_element("id", 'outlined-adornment-weight')
project_field.send_keys("Ashutosh")

client_field = driver.find_element("id", 'clientName')
client_field.click()
client_field.send_keys(Keys.ARROW_DOWN)
client_field.send_keys(Keys.RETURN)

vertical_field = driver.find_element("id", 'clientName')
vertical_field.click()
vertical_field.send_keys(Keys.ARROW_DOWN)
vertical_field.send_keys(Keys.RETURN)

time.sleep(10)


