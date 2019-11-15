import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import os

from Selenium.SampleProjects.Pages.homePage1 import HomePage1
from Selenium.SampleProjects.Pages.loginPage1 import LoginPage1

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))



class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/repos/qatest/Selenium/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(50)

    def test_login_valid(self):
        self.driver.get("http://dev.shahisawari.co/")
        self.driver.set_page_load_timeout(50)
        #object creation
        login = LoginPage1(self.driver)

        time.sleep(2)
        login.enter_email("dev@shahisawari.pk")
        login.enter_password("12345")
        login.click_loginbutton()
        # self.driver.find_element_by_id("exampleInputEmail1").send_keys("dev@shahisawari.pk")
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("exampleInputPassword1").send_keys("12345")
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath("//button[@class='btn btn-block btn-primary mt-lg login-btn']").click()
        # time.sleep(5)
        print("You Logged in Successfully!")

        time.sleep(5)

        #Object creation
        homepage = HomePage1(self.driver)

        homepage.click_Administratorlink()
        time.sleep(1)
        homepage.click_Logoutlink()
        time.sleep(1)
        homepage.click_Yesbutton()
        # self.driver.find_element_by_xpath("//span[contains(text(),'Administrator')]").click()
        # time.sleep(3)
        # self.driver.find_element_by_link_text("Logout").click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        # time.sleep(2)
        print("You Logged out Successfully!")




    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...!")

    def _addSkip(
        self, result: unittest.result.TestResult, test_case: unittest.case.TestCase, reason: str):
        pass


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:/repos/qatest/Selenium/SampleProjects/SP2 reports", verbosity=2))