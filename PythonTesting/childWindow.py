import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()

windowOpened=driver.window_handles
driver.switch_to.window(windowOpened[1])

a2=driver.find_element(By.XPATH,"//div[@class='example']/h3").text
print(a2)
driver.close()
driver.switch_to.window(windowOpened[0])
a=driver.find_element(By.TAG_NAME,"h3").text
print(a)

assert "Opening a new window"==driver.find_element(By.TAG_NAME,"h3").text


































time.sleep(2)