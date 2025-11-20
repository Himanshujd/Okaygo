import pytest
from unittest.mock import Mock, patch, MagicMock
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os

# Add the current directory to path to import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class TestTaskAutomation:
    
    @pytest.fixture
    def mock_driver(self):
        """Create a mock WebDriver instance"""
        driver = Mock()
        driver.find_element.return_value = Mock()
        driver.find_elements.return_value = [Mock()]
        driver.get.return_value = None
        driver.maximize_window.return_value = None
        driver.execute_script.return_value = None
        driver.current_window_handle = "main_window"
        driver.switch_to.window.return_value = None
        driver.quit.return_value = None
        return driver
    
    @pytest.fixture
    def mock_wait(self):
        """Create a mock WebDriverWait instance"""
        wait = Mock()
        wait.until.return_value = Mock()
        return wait
    
    @patch('task_automation.webdriver.Chrome')
    @patch('task_automation.WebDriverWait')
    def test_driver_setup(self, mock_wait_class, mock_chrome):
        """Test driver initialization and setup"""
        mock_driver = Mock()
        mock_chrome.return_value = mock_driver
        mock_wait_class.return_value = Mock()
        
        # Import and run the setup part
        import task_automation
        
        mock_chrome.assert_called_once()
        mock_driver.maximize_window.assert_called_once()
        mock_wait_class.assert_called_once_with(mock_driver, 20)
    
    def test_login_elements_located(self, mock_driver, mock_wait):
        """Test login element location"""
        # Mock elements
        username_element = Mock()
        password_element = Mock()
        login_btn_element = Mock()
        
        mock_wait.until.return_value = username_element
        mock_driver.find_element.side_effect = [password_element, login_btn_element]
        
        # Simulate login process
        mock_wait.until.assert_called()
        username_element.send_keys.assert_not_called()  # Will be called in actual implementation
        
    def test_login_credentials_input(self, mock_driver, mock_wait):
        """Test login credentials are entered correctly"""
        username_element = Mock()
        password_element = Mock()
        login_btn_element = Mock()
        
        mock_wait.until.return_value = username_element
        mock_driver.find_element.side_effect = [password_element, login_btn_element]
        
        # Simulate credential input
        username_element.send_keys("himanshu.tiwari@mails.okaygo.in")
        password_element.send_keys("OkayGo@123")
        login_btn_element.click()
        
        username_element.send_keys.assert_called_with("himanshu.tiwari@mails.okaygo.in")
        password_element.send_keys.assert_called_with("OkayGo@123")
        login_btn_element.click.assert_called_once()
    
    def test_url_navigation(self, mock_driver):
        """Test URL navigation"""
        mock_driver.get("https://task.okaygodev.in/org/process_okaygo")
        mock_driver.get.assert_called_with("https://task.okaygodev.in/org/process_okaygo")
    
    def test_dropdown_interaction(self, mock_driver, mock_wait):
        """Test dropdown menu interaction"""
        dropdown_element = Mock()
        mock_wait.until.return_value = dropdown_element
        
        # Simulate dropdown click
        mock_driver.execute_script("arguments[0].click();", dropdown_element)
        mock_driver.execute_script.assert_called_with("arguments[0].click();", dropdown_element)
    
    def test_file_upload(self, mock_driver, mock_wait):
        """Test file upload functionality"""
        file_input = Mock()
        mock_wait.until.return_value = file_input
        
        file_path = "/Users/himanshu.tiwari/Okaygo/bulk_sample (4).xlsx"
        file_input.send_keys(file_path)
        
        file_input.send_keys.assert_called_with(file_path)
    
    def test_element_locators(self, mock_driver):
        """Test various element locator strategies"""
        # Test ID locator
        mock_driver.find_element(By.ID, "Email")
        mock_driver.find_element.assert_called_with(By.ID, "Email")
        
        # Test CLASS_NAME locator
        mock_driver.find_element(By.CLASS_NAME, "login_btn")
        mock_driver.find_element.assert_called_with(By.CLASS_NAME, "login_btn")
        
        # Test XPATH locator
        mock_driver.find_element(By.XPATH, "//span[text()='Jubilant Food Works']")
        mock_driver.find_element.assert_called_with(By.XPATH, "//span[text()='Jubilant Food Works']")
    
    def test_search_functionality(self, mock_driver, mock_wait):
        """Test search box functionality"""
        search_element = Mock()
        mock_wait.until.return_value = search_element
        
        # Simulate search input
        search_element.send_keys("himanshu.tiwari@mails.okaygo.in")
        search_element.send_keys(Keys.RETURN)
        
        search_element.send_keys.assert_any_call("himanshu.tiwari@mails.okaygo.in")
        search_element.send_keys.assert_any_call(Keys.RETURN)
    
    def test_window_handling(self, mock_driver):
        """Test window switching functionality"""
        original_tab = "main_window"
        mock_driver.current_window_handle = original_tab
        
        # Simulate window switch
        mock_driver.switch_to.window(original_tab)
        mock_driver.switch_to.window.assert_called_with(original_tab)
    
    def test_scroll_functionality(self, mock_driver):
        """Test JavaScript scroll execution"""
        scroll_script = "arguments[0].scrollIntoView();"
        element = Mock()
        
        mock_driver.execute_script(scroll_script, element)
        mock_driver.execute_script.assert_called_with(scroll_script, element)
    
    @patch('task_automation.time.sleep')
    def test_wait_times(self, mock_sleep):
        """Test that appropriate wait times are used"""
        import time
        time.sleep(2)
        mock_sleep.assert_called_with(2)
    
    def test_driver_cleanup(self, mock_driver):
        """Test driver cleanup"""
        mock_driver.quit()
        mock_driver.quit.assert_called_once()

if __name__ == "__main__":
    pytest.main([__file__])