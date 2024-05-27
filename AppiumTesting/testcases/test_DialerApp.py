import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict(


    deviceName='Android',
    platformName='Android',
    appPackage='com.android.dialer',
    appActivity='.BBKTwelveKeyDialer'

)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.find_element(By.ID,'com.android.dialer:id/one').click()
driver.find_element(By.ID,'com.android.dialer:id/two').click()
driver.find_element(By.ID,'com.android.dialer:id/three').click()
driver.find_element(By.ID,'com.android.dialer:id/five').click()

driver.find_element(By.ID,'com.android.dialer:id/dialButtonSim1').click()


time.sleep(2)
driver.quit()
