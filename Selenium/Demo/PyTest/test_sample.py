# Naming convension matters a lot for pytest so file name should start with "test_" or end with "_test"
# To Run the pytest [We can Only ran pytest with terminal/cmd] go to command line / terminal directory>"pytest file_name.py" or "py.test" or "pytest"

import time
from selenium import webdriver
import pytest  # import pytest lib to implement fixtures

class TestSSLogin():   # Class Name should start with capital T in "Test" [Class Naming convension]
    @pytest.fixture()  # Annotate fixtures to run this function every time.
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:/repos/qatest/Selenium/drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get("http://dev.shahisawari.co/")
        yield  # Use to end the test every time with these under commands
        driver.close()
        driver.quit()
        print("Test Completed...!")

    def test_SS_login(self,test_setup):  # Give parameter of setup function to run the setup every time at start
        time.sleep(2)
        driver.find_element_by_id("exampleInputEmail1").send_keys("dev@shahisawari.pk")
        time.sleep(2)
        driver.find_element_by_id("exampleInputPassword1").send_keys("12345")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='btn btn-block btn-primary mt-lg login-btn']").click()
        time.sleep(2)
        print(driver.title)
        x = driver.title
        time.sleep(2)
        assert x == "Shahi Sawari (PVT) LTD - welcome page"

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed...!")
