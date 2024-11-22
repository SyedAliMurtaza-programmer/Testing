from selenium import webdriver
import time
from selenium.webdriver.common.by import By

a = webdriver.ChromeOptions()

#a.add_argument('--start-maximized--')
driver = webdriver.Chrome(options=a)
driver.maximize_window()
driver.get("https://automationexercise.com/")
driver.find_element(By.CSS_SELECTOR,"a[href='/view_cart']").click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
product = driver.find_element(By.XPATH,"//input[@id = 'susbscribe_email']")
product.send_keys('a@gmail.com')
driver.find_element(By.XPATH,"//button[@id='subscribe']").click()

time.sleep(100)