import time

import allure
import openpyxl
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from utilities import dataProvider



@pytest.mark.usefixtures("log_on_failure")
def test_dologin(appium_driver):
    driver = appium_driver
    driver.get("http://google.com")
    driver.find_element_by_xpath("//*[@name='q']").send_keys("Hello Appium !!!")

