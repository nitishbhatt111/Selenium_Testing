import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

sortedList=[]
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

veggieList=driver.find_elements(By.XPATH,"//tr/td[1]");

for ele in veggieList:
    sortedList.append(ele.text)

originalSortList=sortedList.copy()

sortedList.sort()

assert sortedList==originalSortList

time.sleep(3)