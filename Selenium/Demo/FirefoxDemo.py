from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

firefox_options=webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")



# path=r"C:\\Users\\Muhammad Anas\\Downloads\\Drivers\\geckodriver.exe"
path = "../drivers/geckodriver.exe"

driver = webdriver.Firefox(executable_path=path, firefox_options=firefox_options)

driver.set_page_load_timeout(10)
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation Step by step")
time.sleep(2)
#Search button is overlapping with the search list thats why we import Keys class and hit the button.
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
print(driver.title)
driver.close()
driver.quit()
print("Comnpleted...!")
