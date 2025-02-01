from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner
import os

class TestSearchFunctionality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://mihanshop.store")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Test valid product search
    def test_search_valid_product(self):
        search_box = self.driver.find_element(By.NAME, "s")
        search_box.clear()
        search_box.send_keys("test product" + Keys.RETURN)
        time.sleep(2)
        results = self.driver.find_elements(By.CLASS_NAME, "product")
        self.assertGreater(len(results), 0, "No products found for valid search query")

    # Test invalid product search
    def test_search_invalid_product(self):
        search_box = self.driver.find_element(By.NAME, "s")
        search_box.clear()
        search_box.send_keys("nonexistent product" + Keys.RETURN)
        time.sleep(2)
        results = self.driver.find_elements(By.CLASS_NAME, "product")
        self.assertEqual(len(results), 0, "Unexpected products found for an invalid search query")

    # Test empty query search
    def test_search_empty_query(self):
        search_box = self.driver.find_element(By.NAME, "s")
        search_box.clear()
        search_box.send_keys("" + Keys.RETURN)
        time.sleep(2)
        results = self.driver.find_elements(By.CLASS_NAME, "product")
        self.assertGreater(len(results), 0, "No products found for empty search (should return all products)")

    # Test search with special characters
    def test_search_special_characters(self):
        search_box = self.driver.find_element(By.NAME, "s")
        search_box.clear()
        search_box.send_keys("@#$%^&*" + Keys.RETURN)
        time.sleep(2)
        results = self.driver.find_elements(By.CLASS_NAME, "product")
        self.assertEqual(len(results), 0, "Unexpected results found for special characters query")

if __name__ == "__main__":
    os.makedirs("report", exist_ok=True)
    
    report_path = "report/Search_Functionality_Test_Report.html"

    runner = HtmlTestRunner.HTMLTestRunner(
        output="reports", 
        report_name="Search_Functionality_Test_Report",  
        verbosity=2 
    )
    
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestSearchFunctionality))
