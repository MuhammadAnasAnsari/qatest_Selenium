# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class RecordedTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_recorded(self):
        driver = self.driver
        driver.get("http://dev.shahisawari.co/#/page/login")
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_id("exampleInputEmail1").clear()
        driver.find_element_by_id("exampleInputEmail1").send_keys("dev@shahisawari.pk")
        driver.find_element_by_id("exampleInputPassword1").clear()
        driver.find_element_by_id("exampleInputPassword1").send_keys("12345")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Forgot your password?'])[1]/following::button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Main Navigation'])[1]/preceding::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Administrator'])[1]/following::p[3]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Are you sure you want to logout ?'])[1]/following::button[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
