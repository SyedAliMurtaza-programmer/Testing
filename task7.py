from selenium import webdriver
import time
from selenium.webdriver.common.by import By

a = webdriver.ChromeOptions()

#a.add_argument('--start-maximized--')
driver = webdriver.Chrome(options=a)
driver.maximize_window()
driver.get("https://automationexercise.com/")
driver.find_element(By.CSS_SELECTOR,"a[href='/products']").click()
print("i am on products page")
product = driver.find_element(By.CSS_SELECTOR,"a[href='/product_details/1']")
driver.execute_script('arguments[0].scrollIntoView(true)', product)
driver.find_element(By.CSS_SELECTOR,"a[href='/product_details/1']").click()

time.sleep(100)