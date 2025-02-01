import time
import unittest
import HtmlTestRunner
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductListTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store")
        self.driver.maximize_window()
        time.sleep(2)

    def test_product_list_page_loads(self):
        driver = self.driver

        # Click on "همه محصولات" to go to the product list
        product_list_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'همه محصولات')]"))
        )
        product_list_button.click()
        time.sleep(2)

        # Decode the current URL to match Persian text
        decoded_url = urllib.parse.unquote(driver.current_url)
        self.assertIn("همه-محصولات", decoded_url, "Product list page did not load correctly.")

        # **FIX: Wait for product elements to load**
        try:
            products = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product"))  # Update class name if needed
            )
            self.assertGreater(len(products), 0, "No products displayed on the product list page.")
        except:
            self.fail("Products did not load within the expected time.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test_reports"))
