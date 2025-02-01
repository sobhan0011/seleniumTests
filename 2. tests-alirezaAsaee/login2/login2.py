import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import HtmlTestRunner
import os

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def take_screenshot(self, test_name):
        screenshot_path = f"reports/screenshots/{test_name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

    def test_login(self):
        self.driver.get("https://mihanshop.store/my-account/")
        time.sleep(2)

        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.NAME, "login")

        test_username = "test@gmail.com"
        test_password = "test123!"

        username_input.send_keys(test_username)
        password_input.send_keys(test_password)

        login_button.click()
        time.sleep(3)

        try:
            login_button_after = self.driver.find_element(By.NAME, "login")
            screenshot_path = self.take_screenshot('login_failed')
            self.fail(f"Login failed! Screenshot: {screenshot_path}")
        except NoSuchElementException:
            self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    with open("reports/Login_Test_Report.html", "w", encoding="utf-8") as report_file:
        unittest.main(
            testRunner=HtmlTestRunner.HTMLTestRunner(
                stream=report_file,
                output="reports",
                report_name="Login_Test_Report",
                verbosity=2
            )
        )
