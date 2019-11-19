from Selenium.POMDemo.Locators.locators import Locators  # To import Locator class


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        # login Page locators
        self.email_textbox_id = Locators.email_textbox_id  # To access the locators from the locator class
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_on_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
