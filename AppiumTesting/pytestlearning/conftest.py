import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

#
# @pytest.fixture(params=["device1", "device2"], scope="function")
# def appium_driver(request):
#     if request.param == "device1":
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['deviceName'] = 'Android'
#         desired_caps['udid'] = 'emulator-5554'
#         desired_caps['browserName'] = 'Chrome'
#         driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
#     if request.param == "device2":
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['deviceName'] = 'Android'
#         desired_caps['udid'] = '8e006adb'
#         desired_caps['browserName'] = 'Chrome'
#         driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
#
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#     appium_service.stop()

@pytest.fixture(scope="function")
def appium_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['appPackage'] = 'com.goibibo'
    desired_caps['appActivity'] = '.common.HomeActivity'
    desired_caps['noReset'] = True
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")
# def appium_driver():
#     #global appium_service
#     #appium_service = AppiumService()
#     #appium_service.start()
#
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'
#     desired_caps['deviceName'] = 'Android'
#     desired_caps['appPackage'] = 'com.goibibo'
#     desired_caps['appActivity'] = '.common.HomeActivity'
#     desired_caps['noReset'] = True
#     global driver
#     driver = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps)
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#     #appium_service.stop()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
