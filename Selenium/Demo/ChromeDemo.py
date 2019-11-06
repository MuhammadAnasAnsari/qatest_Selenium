from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# To run Chrome script without opening and viewing the browser
# chrome_options = webdriver.ChromeOptions
chrome_options = Options()
chrome_options.add_argument("--headless")

# to disable the browser extensions
chrome_options.add_argument("--disable_extensions")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)
driver.get("https://www.google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.implicitly_wait(2)
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()
print("Completed...!")
