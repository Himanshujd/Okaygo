import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from testcases.scroll_util import ScrollUtil

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['appPackage'] = 'flipboard.app'
desired_caps['appActivity'] = 'flipboard.activities.LaunchActivityAlias'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.find_element_by_id('flipboard.app:id/first_launch_cover_continue').click()

driver.find_elements_by_id('flipboard.app:id/topic_picker_topic_row_topic_tag')[0].click()
driver.find_elements_by_id('flipboard.app:id/topic_picker_topic_row_topic_tag')[1].click()
driver.find_elements_by_id('flipboard.app:id/topic_picker_topic_row_topic_tag')[2].click()
driver.find_element_by_id('flipboard.app:id/topic_picker_continue_button').click()
driver.find_element_by_id('flipboard.app:id/account_login_buttons_skip').click()
time.sleep(2)
ScrollUtil.swipeUp(4,driver)
time.sleep(2)
ScrollUtil.swipeDown(4,driver)
time.sleep(2)
ScrollUtil.swipeLeft(2,driver)
time.sleep(2)
ScrollUtil.swipeRight(2,driver)

time.sleep(2)
driver.quit()
