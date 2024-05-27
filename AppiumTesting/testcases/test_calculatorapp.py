import time

from appium import webdriver

desired_cap = {}
desired_cap['platformName'] = 'Android'
desired_cap['deviceName'] = 'Android'
desired_cap['appPackage'] = 'com.android.bbkcalculator'
desired_cap['appActivity'] = '.Calculator'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
driver.implicitly_wait(5)

driver.find_element_by_accessibility_id('2').click()
driver.find_element_by_id('com.android.bbkcalculator:id/plus').click()
driver.find_element_by_accessibility_id('4').click()
driver.find_element_by_id('com.android.bbkcalculator:id/equal').click()

result = driver.find_element_by_id('com.android.bbkcalculator:id/input_edit').text
print(result)
assert int(result) == 6
time.sleep(2)
driver.quit()
