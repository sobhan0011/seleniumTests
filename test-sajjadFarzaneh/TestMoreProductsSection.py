import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner


class TestMoreProductsSection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store/")
        time.sleep(5)

    def test_more_products_section(self):
        driver = self.driver

        # Click on a product link
        product_link = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/article/div/div/section[3]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[5]/div/div/div/div/div[1]/a/img")
        product_link.click()
        time.sleep(5)

        # Navigate to the "More Products" section
        more_product_link = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/ul/li[4]/a/span")
        more_product_link.click()

        # Locate the "More Products" items container
        more_items_container = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[5]/div[2]/div/div")

        # Count the number of products in the container
        more_items = more_items_container.find_elements(By.CLASS_NAME, "product-wrapper")

        # Assert that there are products in the "More Products" section
        self.assertGreater(len(more_items), 0, "No products found in the 'محصولات بیشتر' section.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
