from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def login(wait, username, password):
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "emailId")))
    email_input.send_keys(username)
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys(password)
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Login_loginButton__14J9m")))
    login_button.click()
