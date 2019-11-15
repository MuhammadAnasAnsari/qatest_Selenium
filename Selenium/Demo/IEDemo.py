import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#to Add desire capabilities of ignore protectedMode settings off
caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
caps["ignoreProtectedModeSettings"] = True

path = "../drivers/IEDriverServer32.exe"
driver = webdriver.Ie(executable_path=path, desired_capabilities=caps)
driver.maximize_window()

driver.set_page_load_timeout(10)
driver.get("https://google.com")
time.sleep(2)
print(driver.title)
driver.implicitly_wait(5)
driver.find_element_by_name("q").send_keys("Automation step by step")
# driver.implicitly_wait(5)
#Search button is overlapping with the search list thats why we import Keys class and hit the button.
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.implicitly_wait(4)
print(driver.title)

driver.close()
driver.quit()
print("Completed...!")
