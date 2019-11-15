from Selenium.SampleProjects.ElementsLocators.ElementsLocators import ElementsLocators


class HomePage1():

    def __init__(self, driver):
        self.driver = driver

        self.Administrator_link_xpath = ElementsLocators.Administrator_link_xpath
        self.Logout_link_Linktext = ElementsLocators.Logout_link_Linktext
        self.Yes_button_xpath = ElementsLocators.Yes_button_xpath

    def click_Administratorlink(self):
        self.driver.find_element_by_xpath(self.Administrator_link_xpath).click()

    def click_Logoutlink(self):
        self.driver.find_element_by_link_text(self.Logout_link_Linktext).click()

    def click_Yesbutton(self):
        self.driver.find_element_by_xpath(self.Yes_button_xpath).click()
