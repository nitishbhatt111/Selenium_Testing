import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name="Nitish"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()

alert=driver.switch_to.alert
alertText=alert.text
print(alertText)
alert.accept()
# alert.dismiss()
assert name in alertText

time.sleep(2)
