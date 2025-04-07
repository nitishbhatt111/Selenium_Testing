
import time

from selenium import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://localhost:63342/Selenium_Testing/Mock%20Test/Week1/Sample1/index.html?_ijt=fle1mh668nqmktqv3se4sedc5k&_ij_reload=RELOAD_ON_SAVE")
driver.find_element(By.ID, "loginForm").click()

driver.find_element(By.ID,"username").send_keys("testuser")
driver.find_element(By.NAME,"password").send_keys("password123")

driver.find_element(By.CSS_SELECTOR,".btn").click()

# driver.find_element(By.XPATH,"//a[@class='link']").click()

















time.sleep(3)