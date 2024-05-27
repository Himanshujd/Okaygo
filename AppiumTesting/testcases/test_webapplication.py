import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = dict(


    deviceName='Android',
    platformName='Android',
    browserName='Chrome'

)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.get("http://google.com")
print(driver.title)
driver.find_element(MobileBy.XPATH,"//*[@name='q']").send_keys("Hello Appium !!!")
#driver.find_element_by_name("q").send_keys("Hello Appium !!!")

time.sleep(2)
driver.quit()
