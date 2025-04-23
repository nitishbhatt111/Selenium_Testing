import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.implicitly_wait(4)

driver.get("http://localhost:63342/Selenium_Testing/Mock%20Test/Week1/Sample2/index.html?_ijt=ofjc3ia5n0oanrpdlcnk83tdr3&_ij_reload=RELOAD_ON_SAVE")




# title=driver.find_element(By.ID,"header").text
# assert title=="Welcome to Selenium Practice"
# driver.find_element(By.ID,"username").send_keys("Nitish")
# driver.find_element(By.ID,"password").send_keys("Bhatt")


# driver.find_element(By.ID,"exampleLink").click()

# select=Select(driver.find_element(By.ID, "dropdown"))
# select.select_by_index(1)

# driver.find_element(By.XPATH,"//option[@value='option2']").click()

# driver.find_element(By.ID,"agree").click()

driver.find_element(By.TAG_NAME,"table")








time.sleep(3)