import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Scroll to Top Button Verification")
@allure.story("Verify the visibility and functionality of the Scroll to Top button")
@allure.severity(allure.severity_level.CRITICAL)
def test_scroll_to_top_button():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open the website and scroll down to the bottom"):
            driver.get("https://mihanshop.store/")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "scrollToTop"))
            )
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        with allure.step("Wait for the Scroll to Top button to appear"):
            scroll_button = driver.find_element(By.CLASS_NAME, "scrollToTop")
            assert scroll_button.is_displayed(), "Scroll to Top button is not visible"

            allure.attach("Scroll to Top button is visible", name="Scroll to Top button visibility", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Click the Scroll to Top button and verify the scroll position"):
            scroll_button.click()

            # Wait for the scroll position to reset to the top
            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script("return window.scrollY;") == 0
            )

            scroll_position = driver.execute_script("return window.scrollY;")
            assert scroll_position == 0, f"Scroll to Top button did not work as expected. Scroll position: {scroll_position}"

            allure.attach(f"Scroll position after clicking the button: {scroll_position}", name="Scroll Position", attachment_type=allure.attachment_type.TEXT)

    finally:
        driver.quit()
