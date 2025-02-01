import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://mihanshop.store")

    # Find and click on the product based on the provided inspect link text
    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "خرید کاغذ a4 ارزان"))
    )
    product_link.click()

    # Verify product details page is loaded
    product_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title"))
    )
    product_price = driver.find_element(By.CSS_SELECTOR, ".product-price")
    time.sleep(2)  # Allow time for the elements to load

    # Check that product details are displayed
    assert product_title.is_displayed() and product_price.is_displayed(), "Product details are not displayed correctly."

    print("Test Passed: Product opened successfully.")

    driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test_reports"))
