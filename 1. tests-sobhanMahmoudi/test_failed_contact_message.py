import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Contact Form Validation")
@allure.story("Verify error message when submitting an empty contact form")
@allure.severity(allure.severity_level.CRITICAL)
def test_contact_form_error():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open the contact page"):
            driver.get("https://mihanshop.store/%D8%AA%D9%85%D8%A7%D8%B3-%D8%A8%D8%A7-%D9%85%D8%A7/")

        with allure.step("Locate form fields and submit button"):
            submit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@type='submit' and @value='ارسال درخواست' and contains(@class, 'wpcf7-submit')]")
                )
            )

        with allure.step("Scroll to and click the submit button"):
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
            actions = ActionChains(driver)
            actions.move_to_element(submit_button).click().perform()

        with allure.step("Verify error message appears"):
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output"))
            )
            actual_error_text = error_message.text
            expected_error_text = "یک یا چند تا از مقادیر وارد شده مشکل دارد، لطفا پس از بررسی دوباره تلاش کنید."

            allure.attach(actual_error_text, name="Actual Error Message", attachment_type=allure.attachment_type.TEXT)
            assert expected_error_text in actual_error_text, f"Error message not as expected. Found: {actual_error_text}"

    finally:
        driver.quit()
