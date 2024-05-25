import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from sympy import true

# Define the desired capabilities
desired_caps =  {
    'deviceName': 'Android',
    'platformName': 'Android',
    'browserName': 'chrome',
    'automationName': 'UiAutomator2',
    'NO_RESET' : True

}

# Setting up the options for UiAutomator2
options = UiAutomator2Options().load_capabilities(desired_caps)


# Try connecting to Appium server
try:
    print("Attempting to connect to Appium server...")
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    print("Connection to Appium server established.")
except Exception as e:
    print(f"Failed to connect to Appium server: {e}")
    exit(1)

# Navigate to Google
try:
    driver.get("http://google.com/")
    print("Navigated to Google.")
except Exception as e:
    print(f"Failed to navigate to Google: {e}")
    driver.quit()
    exit(1)

# Find the search box using XPATH and input text
try:
    search_box = driver.find_element(AppiumBy.XPATH, "//input[@name='q']")
    search_box.send_keys("Hello")
    print("Search box found and text entered.")
except Exception as e:
    print(f"Failed to find the search box or enter text: {e}")
    driver.quit()
    exit(1)

# Print the title of the page
try:
    print(driver.title)
except Exception as e:
    print(f"Failed to retrieve page title: {e}")

# Wait for 2 seconds
time.sleep(2)

# Quit the driver
try:
    driver.quit()
    print("Driver quit successfully.")
except Exception as e:
    print(f"Failed to quit the driver: {e}")
