from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
# Implicit Waits:
driver.implicitly_wait(10)
driver.maximize_window()
# driver.implicitly_wait(2)
driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("Naeem Shehzad")
driver.find_element_by_name("btnK").click()

driver.close()
driver.quit()