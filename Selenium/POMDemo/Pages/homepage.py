from Selenium.POMDemo.Locators.locators import Locators  # To import Locator class


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        # home Page locators
        self.Administrator_link_xpath = Locators.Administrator_link_xpath
        self.Logout_link_linkText = Locators.Logout_link_linkText
        self.Yes_button_xpath = Locators.Yes_button_xpath

    def click_on_Administrator(self):
        self.driver.find_element_by_xpath(self.Administrator_link_xpath).click()

    def click_on_Logout(self):
        self.driver.find_element_by_link_text(self.Logout_link_linkText).click()

    def click_on_Yes(self):
        self.driver.find_element_by_xpath(self.Yes_button_xpath).click()
