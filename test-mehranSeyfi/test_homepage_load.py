from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestHomepageLoad:
    def test_homepage_load(self):
        driver = webdriver.Chrome()
        driver.get("https://mihanshop.store")
        assert "MihanShop" in driver.title  
        print("Homepage loaded and title verified")
        driver.quit()

if __name__ == "__main__":
    pytest.main()
