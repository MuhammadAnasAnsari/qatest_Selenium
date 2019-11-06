import time

from selenium import webdriver

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("Automation Step by step")

driver.implicitly_wait(2)

driver.find_element_by_name('btnK').click()

time.sleep(2)

driver.close()
driver.quit()

print("Test Completed...!")
