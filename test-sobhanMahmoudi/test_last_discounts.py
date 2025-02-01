import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Newsletter Subscription")
@allure.story("Verify subscription with a valid email")
@allure.severity(allure.severity_level.CRITICAL)
def test_newsletter_subscription():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Mihanshop homepage"):
            driver.get("https://mihanshop.store/")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))

        with allure.step("Locate email input and submit button"):
            email_field = driver.find_element(By.XPATH, "//input[@type='email']")
            submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='عضویت']")

        with allure.step("Enter email address"):
            email_field.send_keys("sasdasdas@gmail.com")

        with allure.step("Scroll to and click the submit button"):
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
            actions = ActionChains(driver)
            actions.move_to_element(submit_button).click().perform()

        with allure.step("Verify success message appears"):
            success_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".mc4wp-alert"))
            )
            actual_success_text = success_message.text
            expected_success_text = "لطفاً یک لیست انتخاب کنید."

            # Attach logs to Allure report
            allure.attach(actual_success_text, name="Actual Success Message", attachment_type=allure.attachment_type.TEXT)

            # Capture a screenshot and attach it to Allure report
            driver.save_screenshot("success_screenshot.png")
            allure.attach.file("success_screenshot.png", name="Success Screenshot", attachment_type=allure.attachment_type.PNG)

            assert expected_success_text in actual_success_text, f"Success message not as expected. Found: {actual_success_text}"

    finally:
        driver.quit()
