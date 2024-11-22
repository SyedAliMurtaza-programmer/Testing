from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By

a=webdriver.ChromeOptions()
a.add_argument("--start-maximized")
driver = webdriver.Chrome(options = a)

driver.get("https://automationexercise.com/")
driver.find_element(By.CSS_SELECTOR,"a[href='/login']").click()
driver.find_element(By.XPATH,"//input[@data-qa = 'login-email']").send_keys("sajid112@hotmail.com")
driver.find_element(By.XPATH,"//input[@data-qa = 'login-password']").send_keys("Password")
driver.find_element(By.XPATH,"//button[@data-qa = 'login-button']").click()
driver.find_element(By.CSS_SELECTOR,"a[href='/delete_account']").click()
print("Account is deleted")
#driver.find_element(By.CSS_SELECTOR,"a[@data-qa ='continue-button']").click()




time.sleep(1000)