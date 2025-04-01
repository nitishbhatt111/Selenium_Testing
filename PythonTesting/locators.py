import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Nitish")

driver.find_element(By.NAME, "email").send_keys("nitishbhatt338@gmail.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("ILoveYou")

# driver.find_element(By.ID, "exampleCheck1").click()

# driver.find_element(By.XPATH,"//input[@type='radio']").click()
#
# #// for css selector just use .first if it is a class name and use # if it is id
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


select=Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
select.select_by_index(1)


driver.find_element(By.ID,"inlineRadio2").click()

driver.find_element(By.NAME,"bday").send_keys("25-12-2002")


# // tagname [@attribute='value'] => //input[@type='submit']   ===> creating manual XPATH
# driver.find_element(By.CLASS_NAME,"btn").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

pr=driver.find_element(By.CLASS_NAME,"alert").text
print(pr)

assert "Success" in pr

time.sleep(3)















