import pytest
from selenium.webdriver.common.by import By
from testAddEditJob.jobs_page import JobsPage


def test_create_job(login):
    driver = login
    driver.get("https://www.qa-eflex.okaygo.in/jobsdb/jobConfig/add")
    jobs_page = JobsPage(driver)

    jobs_page.select_project_name("Mettl Invigilator")
    jobs_page.enter_job_title("Sample Job Title")
    jobs_page.select_remote_job()
    jobs_page.select_part_time_full_time()
    jobs_page.select_shift_timing("Morning Shift")
    jobs_page.enter_job_description("This is a sample job description.")

    # # Add assertions to verify successful job creation
    # success_message = driver.find_element(By.XPATH, "//*[text()='Job Created Successfully']")
    # assert success_message.is_displayed(), "Job creation failed: Success message not displayed."
