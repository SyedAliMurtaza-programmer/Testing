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
driver.find_element(By.XPATH,"//input[@id = 'search_product']").send_keys("top")
driver.find_element(By.XPATH,"//button[@id = 'submit_search']").click()
total_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))




time.sleep(100)