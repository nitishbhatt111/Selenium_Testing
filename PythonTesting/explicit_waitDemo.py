import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_list=['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list=[]

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=(len(results))
assert count==3

for result in results:
    actual_list.append(result.find_element(By.XPATH,"h4").text)
    button=result.find_element(By.XPATH,"div/button")
    button.click()

assert actual_list==expected_list

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()


#sum validation

prices=driver.find_elements(By.CSS_SELECTOR," tr td:nth-child(5) p")
sum=0

for price in prices:
    sum=sum+int(price.text)

print(sum)

totalAmount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum==totalAmount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)


discountedAmount=float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAmount>discountedAmount


time.sleep(2)