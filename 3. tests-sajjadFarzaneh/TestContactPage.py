import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner


class TestContactPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_contact_page(self):
        driver = self.driver
        contact_link = driver.find_element(By.XPATH, "/html/body/div[1]/footer/div[1]/aside/div/div/div/section[1]/div/div[1]/div/div/div/ul/li/ul/li[5]/a")
        contact_link.click()

        time.sleep(2)
        contact_form = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/article/div/div/section[1]/div/div[2]")

        self.assertTrue(contact_form.is_displayed(), "Contact form is not displayed.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
