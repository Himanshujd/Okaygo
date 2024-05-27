import time

from appium import webdriver

desired_caps = dict(


    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='.activities.PeopleActivity'

)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_accessibility_id('New Contact').click()
driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()

driver.find_element_by_xpath("//android.widget.EditText[@text='Name']").send_keys("Harry")
driver.find_element_by_xpath("//android.widget.EditText[@text='Phone']").send_keys("9767672")
driver.hide_keyboard()
driver.find_element_by_xpath("//*[contains(@text,'Done')]").click()






time.sleep(2)
driver.quit()
