from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class JobsPage:
    def __init__(self, driver):
        self.driver = driver
        self.project_name_dropdown = (By.XPATH, "//*[@id='projectName']")
        self.job_title_input = (By.XPATH, "//*[@id='outlined-adornment-weight']")
        self.remote_job_radio = (By.XPATH, "//*[@id='root']/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div")
        self.shift_timings_dropdown = (By.XPATH, "//*[@id='ShiftTimings']")
        self.part_time_full_time_radio = (
        By.XPATH, "//*[@id='root']/div/div[3]/div[1]/div/div[1]/div[4]/div[2]/label[3]/input")
        self.job_description_input = (By.XPATH, "//*[@id='root']/div/div[3]/div[1]/div/div[3]/div[1]/div/div/div[2]/div/div/div")

    def select_project_name(self, project_name):
        dropdown = Select(self.driver.find_element(*self.project_name_dropdown))
        dropdown.select_by_visible_text(project_name)

    def enter_job_title(self, job_title):
        self.driver.find_element(*self.job_title_input).send_keys(job_title)

    def select_remote_job(self):
        self.driver.find_element(*self.remote_job_radio).click()

    def select_part_time_full_time(self):
        self.driver.find_element(*self.part_time_full_time_radio).click()

    def select_shift_timing(self, shift_timing):
        dropdown = Select(self.driver.find_element(*self.shift_timings_dropdown))
        dropdown.select_by_visible_text(shift_timing)

    def enter_job_description(self, job_description):
        self.driver.find_element(*self.job_description_input).send_keys(job_description)
