import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Contact Form Submission")
@allure.story("Submit the contact form and verify the success message")
@allure.severity(allure.severity_level.CRITICAL)
def test_contact_form_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open the contact page"):
            driver.get("https://mihanshop.store/%D8%AA%D9%85%D8%A7%D8%B3-%D8%A8%D8%A7-%D9%85%D8%A7/")

        with allure.step("Fill out the contact form fields"):
            name_field = driver.find_element(By.NAME, "your-name")
            email_field = driver.find_element(By.NAME, "your-email")
            subject_field = driver.find_element(By.NAME, "your-subject")
            message_field = driver.find_element(By.NAME, "your-message")
            submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='ارسال درخواست' and contains(@class, 'wpcf7-submit')]")

            email_field.send_keys("sasdasdas@gmail.com")
            name_field.send_keys("John Doe")
            subject_field.send_keys("Test Subject")
            message_field.send_keys("Test Message")

            # Scroll to the submit button
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

        with allure.step("Click the submit button"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
            actions = ActionChains(driver)
            actions.move_to_element(submit_button).click().perform()

        with allure.step("Verify the success message after submission"):
            # Wait for the success message to be visible
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output"))
            )

            actual_success_text = success_message.text
            expected_success_text = "از پیام شما متشکریم، پیام شما با موفقیت ارسال شد."

            # Attach the result of the success message to Allure report
            allure.attach(actual_success_text, name="Actual Success Message", attachment_type=allure.attachment_type.TEXT)

            assert expected_success_text in actual_success_text, f"Success message not as expected. Found: {actual_success_text}"

    finally:
        driver.quit()
