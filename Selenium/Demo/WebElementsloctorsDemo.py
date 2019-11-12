import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #if button is overlapping with the results
from webdriver_manager.chrome import ChromeDriverManager  # to import web deriver mangae for chrome browser

# driver = webdriver.Chrome(ChromeDriverManager().install())  # automatically system will install the chromedriver
driver=webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)

# driver.find_element_by_name("q").send_keys("Automation Selenium python step by step")
searchBox=driver.find_element_by_name("q")
searchBox.send_keys("Muhammad Anas Ansari")

time.sleep(2)
#driver.find_element_by_name("btnK").click()
driver.find_element_by_class_name("gNO89b").send_keys(Keys.ENTER)    #if the button is overlapping with results list

print(driver.title)

driver.find_element_by_xpath("/html/body/div[7]/div[3]/div[5]/div/div/div[1]/div/div/div[1]/div/div[2]/a").click()
time.sleep(10)
driver.close()
driver.quit()
print("Completed...!")
