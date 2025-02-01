import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner


class TestSubmitComment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mihanshop.store/")
        time.sleep(2)

    def test_submit_comment(self):
        driver = self.driver

        product_link = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/article/div/div/section[6]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[7]/div/div/div/div/div[1]/a/img")
        product_link.click()
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/5);")
        time.sleep(2)

        comment_link = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/ul/li[2]/a/span")
        comment_link.click()

        rating_star = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/div/div/form/div/p/span/a[3]")
        rating_star.click()

        comment_box = driver.find_element(By.ID, "comment")
        comment_box.send_keys("این یک کامنت تست است")

        name_box = driver.find_element(By.ID, "author")
        name_box.send_keys("sajjad")

        email_box = driver.find_element(By.ID, "email")
        email_box.send_keys("sajjadfarzane1@gmail.com")

        submit_button = driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/div/div/form/p[6]/input[1]")
        submit_button.click()
        time.sleep(2)

        confirmation_message = driver.find_element(By.CLASS_NAME, "woocommerce-review__awaiting-approval")
        self.assertIn("پس از تایید نمایش داده می شود", confirmation_message.text, "Comment submission failed or confirmation message is missing.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
