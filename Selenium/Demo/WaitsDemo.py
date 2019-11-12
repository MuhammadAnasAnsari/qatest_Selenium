import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait                # for Explicit waits import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC       # For explicit wait expected condition
from selenium.webdriver.common.by import By                            # Import By class to implement expected condition "by" method


# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome("../drivers/chromedriver.exe")
# Implicit Waits:
# driver.implicitly_wait(10)
driver.maximize_window()
# driver.implicitly_wait(2)

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("What is the meaning of Anas?")

wait = WebDriverWait(driver, 10)  # Implement explicit wait by new object and its waits time
try:
    element=wait.until(EC.element_to_be_clickable((By.NAME,"btnK")))  # Implement explicit wait with expected condition wait by class method "Name" its value
    print("element is clickable!")
except:
    print("element is not clickable!")
    exit(1)

element.click()

# driver.find_element_by_name("btnK").click()

time.sleep(10)

print(driver.title)

driver.implicitly_wait(10)
print("Script Completed...!")
driver.close()
driver.quit()
