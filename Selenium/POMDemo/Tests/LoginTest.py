import time
import unittest
from selenium import webdriver


import sys  # Import os,sys classes and " sys.path.append(os.path.join(os.path.dirname(__file__),"..","..")) "
import os  # to run the POM project from command line

from Selenium.POMDemo.Pages.homepage import HomePage
from Selenium.POMDemo.Pages.loginpage import LoginPage

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import HtmlTestRunner


# from webdriver_manager.chrome import ChromeDriverManager


class logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/repos/qatest/Selenium/drivers/chromedriver.exe")
        # cls.driver=webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(50)

    def test_SS_Devlogin_valid(self):
        # Login to Dev Panel of Shahi Sawari

        self.driver.get("http://dev.shahisawari.co/")

        time.sleep(2)
        login = LoginPage(self.driver)

        login.enter_email("dev@shahisawari.pk")
        time.sleep(1)
        login.enter_password("12345")

        login.click_on_login()
        time.sleep(3)
        print("You Logged in Successfull!")

        time.sleep(3)
        homepage = HomePage(self.driver)
        time.sleep(1)
        homepage.click_on_Administrator()
        time.sleep(1)
        homepage.click_on_Logout()
        time.sleep(1)
        homepage.click_on_Yes()
        time.sleep(1)
        print("You Logged out Successfully!")
        # self.driver.set_page_load_timeout(20)
        # self.driver.find_element_by_id("exampleInputEmail1").send_keys("dev@shahisawari.pk")
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("exampleInputPassword1").send_keys("12345")
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath("//button[@class='btn btn-block btn-primary mt-lg login-btn']").click()
        # time.sleep(5)
        # print("You Logged in Successfully!")

        # Logout to the Dev Panel of Shahi Sawari
        # self.driver.find_element_by_xpath("//span[contains(text(),'Administrator')]").click()
        # self.driver.find_element_by_link_text("Logout").click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        # time.sleep(5)
        # print("You Logged out Successfully!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed...!")


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="E:/repos/qatest/Selenium/ReportsPOMDemo", verbosity=2))
