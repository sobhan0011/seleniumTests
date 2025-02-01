import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import HtmlTestRunner
import os

class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def take_screenshot(self, test_name):
        screenshot_path = f"reports/screenshots/{test_name}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path

    def test_registration(self):
        self.driver.get("https://mihanshop.store/my-account/")
        time.sleep(2)

        register_button = self.driver.find_element(By.CLASS_NAME, "wd-switch-to-register")
        register_button.click()
        time.sleep(2)

        email_input = self.driver.find_element(By.ID, "reg_email")
        password_input = self.driver.find_element(By.ID, "reg_password")

        test_email = "testuser1@gmail.com"
        test_password = "StrongPassword123!"
        email_input.send_keys(test_email)
        password_input.send_keys(test_password)

        register_submit_button = self.driver.find_element(By.NAME, "register")
        register_submit_button.click()
        time.sleep(3)

        try:
            self.driver.find_element(By.NAME, "register")
            screenshot_path = self.take_screenshot('registration_failed')
            self.fail(f"Registration failed! Screenshot: {screenshot_path}")
        except NoSuchElementException:
            print("Registration successful!")
            self.assertTrue(True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    with open("reports/Registration_Test_Report.html", "w", encoding="utf-8") as report_file:
        unittest.main(
            testRunner=HtmlTestRunner.HTMLTestRunner(
                stream=report_file,
                output="reports",
                report_name="Registration_Test_Report",
                verbosity=2
            )
        )
