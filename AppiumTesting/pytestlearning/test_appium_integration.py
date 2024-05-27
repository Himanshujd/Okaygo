import time

import allure
import openpyxl
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from testcases.scroll_util import ScrollUtil
from utilities import dataProvider


#
# @pytest.skip
# @pytest.mark.usefixtures("log_on_failure")
# @pytest.mark.parametrize("city,country", dataProvider.get_data("SearchTest"))
# def test_dologin(city,country,appium_driver):
#     driver = appium_driver
#     driver.find_element_by_id('com.goibibo:id/btn1').click()
#     driver.find_element_by_accessibility_id('destination').click()
#     driver.find_element_by_id('com.goibibo:id/edtSearch').send_keys(city)
#     driver.find_elements_by_id('com.goibibo:id/lytLocationItem')[0].click()
#     driver.find_element_by_xpath("//android.widget.TextView[@text='Search']").click()
#     cityText = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'EXPLORE')]").text
#     print(cityText)
#     newCityText = str(cityText).replace("EXPLORE ","").replace("!","")
#     print(newCityText)
#
#     assert newCityText in str(city).upper()
#     #allure.attach(driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)




def test_searchVillas(appium_driver):
    driver = appium_driver
    driver.find_element_by_xpath("//android.widget.TextView[@text='Villas & Apts']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='Area, Landmark or Property']").click()
    driver.find_element_by_id('com.goibibo:id/edtSearch').send_keys("Delhi")
    driver.hide_keyboard()
    #driver.find_elements_by_id('com.goibibo:id/lytLocationItem')[0].click()
    #driver.find_element_by_xpath("//android.widget.TextView[@text='6']").click()
    #driver.find_element_by_xpath("//android.widget.TextView[@text='11']").click()
    #driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Continue')]").click()
    #driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'View Stays')]").click()
    #ScrollUtil.scrollToTextByAndroidUIAutomator("Shubham Vilas", driver)