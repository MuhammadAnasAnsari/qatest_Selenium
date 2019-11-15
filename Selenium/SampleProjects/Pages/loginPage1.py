from Selenium.SampleProjects.ElementsLocators.ElementsLocators import ElementsLocators


class LoginPage1():
    def __init__(self,driver):
        self.driver=driver

        self.email_textbox_id = ElementsLocators.email_textbox_id
        self.password_textbox_id = ElementsLocators.password_textbox_id
        self.login_button_xpath =  ElementsLocators.login_button_xpath

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()




