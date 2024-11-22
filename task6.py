from selenium import webdriver
import time
from selenium.webdriver.common.by import By

a = webdriver.ChromeOptions()
a.add_argument('--start-maximized--')
driver = webdriver.Chrome(options=a)
driver.get("https://automationexercise.com/")
driver.find_element(By.CSS_SELECTOR,"a[href='/test_cases']").click()
print("i am on test case page")
time.sleep(100)