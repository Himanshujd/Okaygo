import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
desired_caps = dict( deviceName='Android',
                     platformName='Android',
                     browserName='Chrome' )


driver = webdriver.Remote('http://127.0.0.1:4723/', desired_caps)
driver.get("http://pl.wikipedia.org")
print(driver.title)

time.sleep(2)

driver.quit()