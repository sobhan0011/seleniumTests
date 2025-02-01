import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


@allure.feature("Category Selection")
@allure.story("Verify category selection from dropdown")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("expected_title", ["اکسسوری"])
def test_category_selection(expected_title):
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open Mihanshop website"):
            driver.get("https://mihanshop.store/")
            time.sleep(5)

        with allure.step("Hover over the dropdown menu"):
            dropdown = driver.find_element(By.CSS_SELECTOR, ".menu-opener-icon")
            actions = ActionChains(driver)
            actions.move_to_element(dropdown).perform()
            driver.implicitly_wait(2)

        with allure.step("Select the 'اکسسوری' category"):
            option = driver.find_element(By.CSS_SELECTOR, "#menu-item-11499")
            option.click()
            time.sleep(5)

        with allure.step("Verify the page title"):
            value = driver.find_element(By.CSS_SELECTOR, ".entry-title").text
            allure.attach(value, name="Extracted Title", attachment_type=allure.attachment_type.TEXT)
            assert value == expected_title, f"Expected '{expected_title}', but got '{value}'"

    finally:
        driver.quit()
