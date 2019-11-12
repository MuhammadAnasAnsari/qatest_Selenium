import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearch(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            # cls.driver=webdriver.Chrome(ChromeDriverManager().install())
            cls.driver = webdriver.Chrome("../drivers/chromedriver.exe")
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()
            print(cls.driver.title)

        def test_search(self):
            self.driver.get("https://www.google.com")

            self.driver.find_element_by_name("q").send_keys("Automation Step by Step")

            self.driver.find_element_by_name("btnK").click()
            print(self.driver.title)

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed....!")

if __name__ == '__main__':
    unittest.main()
