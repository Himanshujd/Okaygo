from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the form page
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Fill in the form
driver.find_element(By.ID, "firstName").send_keys("Himanshu")
driver.find_element(By.ID, "lastName").send_keys("Tiwari")
driver.find_element(By.ID, "userEmail").send_keys("himanshu@example.com")

# Select Gender (Radio Button)
driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()

# Enter Mobile Number
driver.find_element(By.ID, "userNumber").send_keys("9876543210")

# Scroll to make the date field visible
driver.execute_script("window.scrollTo(0, 500)")

# Select Date of Birth
driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.XPATH, "//div[@class='react-datepicker__year-select']/option[@value='1995']").click()
driver.find_element(By.XPATH, "//div[@class='react-datepicker__month-select']/option[@value='5']").click()
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day--015')]").click()

# Enter Subjects
subject_field = driver.find_element(By.ID, "subjectsInput")
subject_field.send_keys("Maths")
subject_field.send_keys(Keys.RETURN)

# Select Hobbies
driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]").click()

# Scroll down to submit button
driver.execute_script("window.scrollTo(0, 800)")

# Upload a file (Assuming there's a file on Desktop)
driver.find_element(By.ID, "uploadPicture").send_keys("/Users/himanshu/Desktop/sample.jpg")

# Enter Address
driver.find_element(By.ID, "currentAddress").send_keys("123 Test Street, Uttarakhand")

# Submit the form
driver.find_element(By.ID, "submit").click()

# Wait for confirmation message
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

print("✅ Form Submitted Successfully!")

# Close the driver
time.sleep(5)  # Pause to verify before closing
driver.quit()
