import HtmlTestRunner                                          # for Html Test runner reports generation
import unittest                                                # for unit test package
from selenium import webdriver                                 # For selnium webdriver package
from webdriver_manager.chrome import ChromeDriverManager       # for chrome driver manager
from selenium.webdriver.common.keys import Keys                # for button element finding when its overlapping with results list



class MyTestCase(unittest.TestCase):

    @classmethod # To Annotate
    def setUpClass(cls):    # Use to setup once for all the test [not opening the browser for every test start seperately]
        cls.driver=webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def setUp(self):  # To Initial Setup before every test
    #
    #   self.driver = webdriver.Chrome("../drivers/chromedriver.exe")
    #   # self.driver=webdriver.Chrome(ChromeDriverManager.install(self))
    #   self.driver.implicitly_wait(10)
    #   self.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("q").send_keys("Muhammad Anas Ansari")
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("btnK").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//a[@class='q qs'][contains(text(),'Images')]").click()
        # self.driver.implicitly_wait(200)
        x = self.driver.title
        print(x)

        self.assertEqual(x,"Muhammad Anas Ansari - Google Search")



    def test_search_2(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name("q").send_keys("World's Best Automation Engineer")
        self.driver.implicitly_wait(20)
        # self.driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
        self.driver.find_element_by_class_name("gNO89b").send_keys(
            Keys.ENTER)  # if the button is overlapping with results list
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//a[@class='q qs'][contains(text(),'Images')]").click()
        # self.driver.implicitly_wait(200)
        x = self.driver.title
        print(x)

        self.assertEqual(x,"World's Best Automation Engineer - Google Search")  # To match the actual results with given expected result


    @unittest.skip("This is a skipped test.")  # To the test failed
    def test_skip(self):
        """ This test should be skipped. """
        pass


    # def tearDown(self):  # To do something after every test
    #     self.driver.close()
    #     self.driver.quit()

    @classmethod # to Annotate
    def tearDownClass(cls):      #Use to close browser once after all test runs [not for every test run]
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':     # Use to run the test from command line
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Flo-DataScience/PycharmProjects/Selenium/Reports'),verbosity=2) # change the "\" to "/" or "\\"
    # unittest.main(verbosity=2) # no need now with above line

# When Run from Command line then directory>python -v file_name.py [for additional informations in command line insimple for Logging]