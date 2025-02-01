from selenium import webdriver
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver  
    driver.quit()  

class TestResponsiveLayout:
    @pytest.mark.parametrize("width, height", [(1920, 1080), (768, 1024), (375, 667)])  # Desktop, tablet, mobile sizes
    def test_responsive_layout(self, driver, width, height):
        driver.set_window_size(width, height)  # Resize window
        driver.get("https://mihanshop.store")
        time.sleep(2)
        
        # Ensure page is fully loaded
        assert driver.execute_script("return document.readyState") == "complete"
        print(f"Page tested on {width}x{height} resolution")
        driver.quit()

if __name__ == "__main__":
    pytest.main()
