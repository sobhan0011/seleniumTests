import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMihanShop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mihanshop.store")

    def test_product_page_navigation(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        try:
            # Click the product link
            product_link = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, '/product/%d8%ae%d8%b1%db%8c%d8%af-%da%a9%d8%a7%d8%ba%d8%b0-a4-%d8%a7%d8%b1%d8%b2%d8%a7%d9%86/')]")
            ))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", product_link)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", product_link)

            # Wait for URL to change
            time.sleep(3)
            current_url = driver.current_url

            # Verify if the URL contains "/product/"
            self.assertIn("/product/", current_url, "Navigation to product page failed!")

            print("✅ Test Passed: Successfully navigated to the product page.")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test_reports"))
