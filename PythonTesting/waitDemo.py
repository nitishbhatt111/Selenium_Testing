import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")

time.sleep(2)

results=driver.find_elements(By.XPATH,"//div[@class='products']/div")

count=(len(results))

assert count==3

for result in results:
    button=result.find_element(By.XPATH,"div/button")
    button.click()


driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

print(driver.find_element(By.CLASS_NAME,"promoInfo").text)


















time.sleep(2)