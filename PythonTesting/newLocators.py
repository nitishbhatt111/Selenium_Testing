import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.CLASS_NAME,"btn1").click()

driver.find_element(By.ID,"firstName").send_keys("nitish")
driver.find_element(By.ID,"lastName").send_keys("bhatt")
driver.find_element(By.ID,"userEmail").send_keys("bhatt123@gmail.com")
driver.find_element(By.ID,"userMobile").send_keys("9876543211")

select=Select(driver.find_element(By.CLASS_NAME,"ng-touched"))
select.select_by_index(2)

driver.find_element(By.XPATH,"//input[@type='radio']")

driver.find_element(By.ID,"userPassword").send_keys("123456")
driver.find_element(By.ID, "confirmPassword").send_keys("123456")

driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

driver.find_element(By.ID, "login").click()


time.sleep(2)