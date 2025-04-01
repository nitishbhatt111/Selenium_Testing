import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com")

driver.maximize_window()
title=driver.title
print(title)
url=driver.current_url
print(url)










time.sleep(2)