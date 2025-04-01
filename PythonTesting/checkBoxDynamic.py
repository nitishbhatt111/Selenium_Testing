import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# checkBox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(len(checkBox))
#
# for check in checkBox:
#     if check.get_attribute("value") == "option2":
#         check.click()
#         assert check.is_selected()
#         break


# radioButton=driver.find_elements(By.CSS_SELECTOR,".radioButton")
# print(len(radioButton))
# for click in radioButton:
#     if click.get_attribute("value")=="radio2":
#         click.click()
#         assert click.is_selected()
#         break

# both ways will work fine
# radioButton[1].click()
# assert radioButton[1].is_selected()



assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

















time.sleep(2)
