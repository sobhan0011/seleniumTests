from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestKeyElementsPresence:
    def test_key_elements(self):
        driver = webdriver.Chrome()
        driver.get("https://mihanshop.store")
        
        # Ensure header and footer are visible
        assert driver.find_element(By.TAG_NAME, "header").is_displayed()
        assert driver.find_element(By.TAG_NAME, "footer").is_displayed()
        
        # Ensure there is at least one link on the page
        assert len(driver.find_elements(By.TAG_NAME, "a")) > 0
        print("Key elements (header, footer, links) are visible")
        driver.quit()

if __name__ == "__main__":
    pytest.main()
