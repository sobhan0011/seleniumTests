from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestBasicForm:
    def test_basic_form(self):
        driver = webdriver.Chrome()
        driver.get("https://mihanshop.store")
        
        # Find and verify a form exists on the page
        form = driver.find_element(By.TAG_NAME, "form")
        assert form.is_displayed(), "Form is not visible"
        
        # Submit the form
        form.submit()
        time.sleep(2)
        
        # Verify the page reloads or success
        assert driver.execute_script("return document.readyState") == "complete"
        print("Basic form presence and submission tested")
        driver.quit()

if __name__ == "__main__":
    pytest.main()
