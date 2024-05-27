import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'com.mobeta.android.demodslv'
desired_caps['appActivity'] = '.Launcher'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.find_elements(By.ID,'com.mobeta.android.demodslv:id/activity_title')[0].click()
#driver.find_elements_by_id('com.mobeta.android.demodslv:id/activity_title')[0].click()

elements = driver.find_elements_by_id('com.mobeta.android.demodslv:id/drag_handle')

actions = TouchAction(driver)
actions.press(elements[0]).wait(3000).move_to(elements[3]).perform().release()

time.sleep(2)
driver.quit()