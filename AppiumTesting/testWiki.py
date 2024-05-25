import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.select import Select

desired_caps = dict(


    deviceName='Android',
    platformName='Android',
    browserName='Chrome'

)

appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)



driver = webdriver.Remote('http://127.0.0.1:4723',desired_caps)

driver.get("http://wikipedia.org")
print(driver.title)
dropdown = driver.find_element_by_css_selector('#searchLanguage')
select = Select(dropdown)
select.select_by_value("hi")

options = driver.find_elements_by_tag_name('option')

print(len(options))

for option in options:
    print("Text is : ",option.text," Lang is: ",option.get_attribute('Lang'))




time.sleep(2)
driver.quit()

appium_service.stop()

