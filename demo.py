from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver  =webdriver.Chrome
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("www.google.com")



name = wait.until(EC.presence_of_element_located((By.XPATH, "")))