import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductQuantity(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store")

    def test_quantity_update_in_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to the first product page
            first_product = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-item")))
            first_product.click()

            # Wait for the quantity input to be available
            quantity_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "quantity-input")))
            quantity_input.clear()
            quantity_input.send_keys("2")

            # Add to cart
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart-btn")))
            add_to_cart_button.click()

            # Verify quantity in cart
            cart_quantity = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-quantity")))

            time.sleep(2)

            # Assert that the quantity displayed in the cart is correct
            self.assertEqual(cart_quantity.text, "2", f"Product quantity in cart is incorrect: {cart_quantity.text}")

            print("✅ Test Passed: Product quantity updated correctly before adding to cart.")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test_reports"))
