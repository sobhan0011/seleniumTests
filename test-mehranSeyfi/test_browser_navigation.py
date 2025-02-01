from selenium import webdriver
import time
import pytest

class TestBrowserNavigation:
    def test_navigation(self):
        driver = webdriver.Chrome()
        driver.get("https://mihanshop.store")

        # Store initial title
        initial_title = driver.title

        # Navigate to another page
        driver.get("https://mihanshop.store/%d8%aa%d9%85%d8%a7%d8%b3-%d8%a8%d8%a7-%d9%85%d8%a7/")
        time.sleep(2)

        # Go back to the previous page
        driver.back()
        time.sleep(2)

        # Ensure the page has returned to the initial page (by title)
        assert driver.title == initial_title, "Title mismatch after going back"
        print("Back navigation test passed by title verification")

        # Go forward to the next page
        driver.forward()
        time.sleep(2)

        # Ensure the page has moved forward to the correct page (by title)
        assert driver.title != initial_title, "Title mismatch after going forward"
        print("Forward navigation test passed by title verification")

        driver.quit()

if __name__ == "__main__":
    pytest.main()
