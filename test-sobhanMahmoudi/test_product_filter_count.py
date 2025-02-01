import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Product Page Verification")
@allure.story("Verify that the number of products per page is 24 or fewer")
@allure.severity(allure.severity_level.CRITICAL)
def test_products_per_page():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        with allure.step("Open the product page"):
            driver.get('https://mihanshop.store/%d9%87%d9%85%d9%87-%d9%85%d8%ad%d8%b5%d9%88%d9%84%d8%a7%d8%aa/')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.per-page-variation'))
            )

        with allure.step("Click '24 products per page' option"):
            elements = driver.find_elements(By.CSS_SELECTOR, '.per-page-variation')
            per_page_24 = elements[1]
            per_page_24.click()

        with allure.step("Wait for the page to load and verify the number of products"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.current-variation > span'))
            )

            per_page_number = driver.find_element(By.CSS_SELECTOR, '.current-variation > span').text
            allure.attach(per_page_number, name="Selected Per Page Number", attachment_type=allure.attachment_type.TEXT)

            # Get the total number of products displayed
            grids = len(driver.find_elements(By.CSS_SELECTOR, '.product-grid-item'))
            allure.attach(f"Number of products: {grids}", name="Number of Products", attachment_type=allure.attachment_type.TEXT)

            # Check that the number of products is 24 or fewer
            assert grids <= 24, f"More than 24 items on the page. Found: {grids} items."

    finally:
        driver.quit()
