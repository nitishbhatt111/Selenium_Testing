import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productsName = product.find_element(By.XPATH, "div/h4/a").text
    if productsName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

driver.find_element(By.ID,"country").send_keys("Ind");

waits=WebDriverWait(driver, 10)
waits.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR,"input[class*='btn']").click()

alertText= driver.find_element(By.CSS_SELECTOR,"div[class*='alert']").text
print(alertText)

assert "Success! Thank you! " in alertText

driver.close()


time.sleep(2)


