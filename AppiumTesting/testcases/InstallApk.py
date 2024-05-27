import time
from pathlib import Path

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {}
desired_cap['platformName'] = 'Android'
desired_cap['deviceName'] = 'Android'
desired_cap['app'] = str(Path().absolute().parent)+'\\app\\drag.apk'
#desired_cap['app'] = str(Path().absolute().parent)+'\\app\\amazon.apk'
#desired_cap['appPackage'] = 'in.amazon.mShop.android.shopping'
#desired_cap['appActivity'] = 'com.amazon.mShop.home.HomeActivity'



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
driver.implicitly_wait(5)
time.sleep(5)

#el1 = driver.find_element_by_id("in.amazon.mShop.android.shopping:id/sso_continue")
#el1.click()
#driver.find_element_by_id('in.amazon.mShop.android.shopping:id/sso_continue').click()
#driver.find_element(By.ID,'in.amazon.mShop.android.shopping:id/sso_continue').click()
#driver.find_element(AppiumBy.ACCESSIBILITY_ID('Continue in English')).click()
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR('new UiSelector().text("Skip sign in")')).click()
# driver.find_element_by_id('in.amazon.mShop.android.shopping:id/skip_sign_in_button').click()
# driver.find_element_by_id('in.amazon.mShop.android.shopping:id/rs_search_src_text').click()
#
# wait = WebDriverWait(driver,10)
# wait.until(EC.element_to_be_clickable((By.ID,'in.amazon.mShop.android.shopping:id/rs_search_src_text')))
# driver.find_element_by_id('in.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys('Shoes')
# driver.press_keycode(66)
time.sleep(5)
driver.quit()
