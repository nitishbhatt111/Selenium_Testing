from selenium import webdriver

chrome_options=webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless") #headless doesn't open any chrome browser and run the cases and print the output
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
