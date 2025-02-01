import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner


class TestFavoriteProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store/")
        time.sleep(3)

    def test_favorite_products(self):
        driver = self.driver

        product_link = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/article/div/div/section[6]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[7]/div/div/div/div/div[1]/a/img")
        product_link.click()
        time.sleep(2)

        favorite_button = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[5]/a/span")
        favorite_button.click()
        time.sleep(5)

        favorite_items_link = driver.find_element(By.XPATH,
            "/html/body/div[1]/header/div/div[2]/div/div/div[3]/div[2]/a")
        favorite_items_link.click()
        time.sleep(2)

        favorite_items_container = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div")
        favorite_items = favorite_items_container.find_elements(By.CLASS_NAME, "wd-wishlist-product-actions")

        self.assertGreater(len(favorite_items), 0, "The favorite items page is empty.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
