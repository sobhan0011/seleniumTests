import unittest
from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner

class TestPageScroll(unittest.TestCase):

    def test_page_scroll(self):
        driver = webdriver.Chrome()
        driver.get("https://mihanshop.store")
     
        initial_position = driver.execute_script("return window.scrollY")
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) 
        
        new_position = driver.execute_script("return window.scrollY")
        
        self.assertGreater(new_position, initial_position)
        print("Page is scrollable")
        driver.quit()

if __name__ == "__main__":
  
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPageScroll)
    
    with open("test_report.html", "w") as report_file:
        runner = HTMLTestRunner(stream=report_file, verbosity=2)
        runner.run(suite)
