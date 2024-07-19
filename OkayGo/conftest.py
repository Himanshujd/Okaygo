import pytest
from selenium import webdriver
from login.login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver):
    driver.get("https://www.qa-eflex.okaygo.in/login")
    login_page = LoginPage(driver)
    login_page.login("himanshu007", "Himanshu@123")
    yield driver
