import time
import unittest
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestImageLoading(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store")

    def test_homepage_image_loading(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Wait for the first image to load (let's try to find the first image element)
            image_element = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "img")))  # Look for the first <img> tag

            # Get the 'src' attribute of the image
            image_src = image_element.get_attribute("src")

            # Verify that the image has a valid src (i.e., not empty)
            self.assertTrue(image_src.startswith("http"), "Image did not load correctly (invalid src attribute).")

            print("✅ Test Passed: Homepage image is loaded correctly.")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test_reports"))
