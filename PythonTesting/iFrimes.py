import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")


driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Hello Brother")

driver.switch_to.default_content()
a=driver.find_element(By.XPATH,"//div[@class='example']/h3").text
print(a)



time.sleep(2)