import time
import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()

@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 15)

def generate_phone_number():
    return str(random.choice([6, 7, 8, 9])) + str(random.randint(100000000, 999999999))

def generate_random_name():
    first = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 7))).capitalize()
    last = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 7))).capitalize()
    return f"{first} {last}"

@pytest.fixture(scope="session")
def phone_number():
    return generate_phone_number()

class TestUserJourney:
    def test_01_login(self, driver, wait, phone_number):
        driver.get("https://pagerouter.d3n8zbjecj5azg.amplifyapp.com/")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Use more robust selectors
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login') or contains(text(), 'Sign in')]|//div[contains(@class, 'login')]//button")))
        login_button.click()

        phone_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your Phone Number' or @type='tel']")))
        phone_input.clear()
        phone_input.send_keys(phone_number)

        send_otp_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Send OTP') or contains(text(),'Send')]")))
        send_otp_btn.click()

        # Wait for OTP input to appear
        otp_inputs = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@maxlength='1' and (@inputmode='numeric' or @type='text')]")))
        otp = "1234"  # Note: This should be configurable for different environments
        assert len(otp_inputs) >= len(otp), f"Expected at least {len(otp)} OTP inputs, found {len(otp_inputs)}"
        
        for i, digit in enumerate(otp):
            otp_inputs[i].clear()
            otp_inputs[i].send_keys(digit)

        verify_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'VERIFY') or contains(text(), 'Verify')]")))
        verify_btn.click()
        
        # Verify login success
        try:
            wait.until(EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your full name']")),
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Find Jobs')]"))
            ))
        except TimeoutException:
            pytest.fail("Login failed - neither onboarding nor dashboard appeared")

    def test_02_onboarding(self, driver, wait):
        # Check if onboarding is needed
        try:
            full_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your full name']")))
        except TimeoutException:
            pytest.skip("Onboarding not required - user already onboarded")
            
        full_name_input.clear()
        full_name_input.send_keys(generate_random_name())

        # More flexible location selector
        location_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'location') or contains(text(), 'location')]|//select|//input[@placeholder*='location' or @placeholder*='Location']")))
        location_input.click()

        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit') or contains(text(), 'Continue') or @type='submit']")))
        submit_btn.click()
        
        # Verify onboarding completion
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Find Jobs')]")))

    def test_03_find_and_apply_job(self, driver, wait):
        # Navigate to jobs if not already there
        try:
            find_jobs_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Find Jobs') or contains(text(),'Jobs')]")))
            find_jobs_tab.click()
        except TimeoutException:
            pass  # Already on jobs page

        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1|//h2|//div[contains(@class, 'job')]|//button[contains(@class, 'filter')]")))
        
        # Scroll to filters section
        try:
            vertical_anchor = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Filter')] | //h2[contains(text(), 'Jobs')] | //div[contains(@class, 'filter')]")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", vertical_anchor)
            time.sleep(2)
        except TimeoutException:
            pass

        attempted = set()
        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                # Find filter buttons (excluding 'All')
                vertical_buttons = driver.find_elements(By.XPATH, "//button[not(contains(., 'All')) and (contains(@class, 'filter') or parent::div[contains(@class, 'filter')])]") or \
                                 driver.find_elements(By.XPATH, "//button[not(contains(., 'All'))]")
                
                if not vertical_buttons:
                    print(f"Attempt {attempt + 1}: No filter buttons found")
                    continue
                    
                random.shuffle(vertical_buttons)

                for vertical in vertical_buttons[:3]:  # Limit to first 3 buttons
                    text = vertical.text.strip()
                    if not text or text in attempted:
                        continue

                    attempted.add(text)

                    try:
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", vertical)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(vertical)).click()
                        time.sleep(2)
                        
                        # Look for job cards with multiple selectors
                        job_cards = None
                        selectors = [
                            "//button[contains(@class, 'rounded-full') and contains(@class, 'bg-white')]",
                            "//div[contains(@class, 'job-card') or contains(@class, 'job')]",
                            "//button[contains(@class, 'job') or contains(@class, 'card')]",
                            "//div[contains(@class, 'card')]"
                        ]
                        
                        for selector in selectors:
                            try:
                                job_cards = WebDriverWait(driver, 5).until(
                                    EC.presence_of_all_elements_located((By.XPATH, selector))
                                )
                                if job_cards:
                                    break
                            except TimeoutException:
                                continue

                        if job_cards:
                            print(f"Found {len(job_cards)} jobs in vertical: {text}")
                            random.choice(job_cards).click()
                            print("Job card clicked successfully")
                            return
                        else:
                            print(f"No jobs found in vertical: {text}")
                            
                    except Exception as e:
                        print(f"Error with vertical {text}: {e}")
                        continue
                        
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(2)

        # Final fallback - try to find any clickable job element
        try:
            any_job = driver.find_element(By.XPATH, "//div[contains(text(), 'job') or contains(text(), 'Job')] | //button[contains(@class, 'apply') or contains(text(), 'Apply')]")
            any_job.click()
            print("Clicked fallback job element")
            return
        except NoSuchElementException:
            pass
            
        driver.save_screenshot("no_jobs_found.png")
        pytest.fail("No jobs found after all attempts")
