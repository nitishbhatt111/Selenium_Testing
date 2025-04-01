import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

# driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#
# driver.find_element(By.XPATH,"//input[@type='email']").send_keys("demo@gmail.com")
# driver.find_element(By.XPATH,"//input[@type='password']").send_keys("87654321")
# driver.find_element(By.ID,"confirmPassword").send_keys("87654321")
#
# driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
#

driver.find_element(By.ID, "userEmail").send_keys("demo@gmail.com")

driver.find_element(By.XPATH,"//input[@type='password']").send_keys("87654321")
driver.find_element(By.CSS_SELECTOR,"input[value='Login']").click()





time.sleep(2)