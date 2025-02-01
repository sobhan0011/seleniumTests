import time
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CategoryFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store")
        self.driver.maximize_window()

    def test_category_filter(self):
        driver = self.driver

        # Wait for the category section to load
        category_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "woodmart-title-container"))
        )

        # Scroll to the category section
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", category_section)
        time.sleep(2)

        # Find and click a category using corrected XPath
        category_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//a[contains(@href, 'product-category/%d9%86%d8%b1%d9%85-%d8%a7%d9%81%d8%b2"
                                        "%d8%a7%d8%b1') and contains(@class, 'category-link')]"))
        )

        # Click the category
        driver.execute_script("arguments[0].click();", category_link)

        # Wait until the category page loads
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "products"))  # Adjust if needed
        )

        # Verify category page loaded successfully
        current_url = driver.current_url
        assert "product-category" in current_url, f"Category page did not load correctly. Current URL: {current_url}"

        print("Test Passed: Category filter is working.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test_reports"))
