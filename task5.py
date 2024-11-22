from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

a = webdriver.ChromeOptions()
a.add_argument('--start-maximized--')
driver = webdriver.Chrome(options=a)
driver.get("https://automationexercise.com/")
driver.find_element(By.CSS_SELECTOR,"a[href='/contact_us']").click()
driver.find_element(By.XPATH,"//input[@data-qa= 'name']").send_keys('Salman Nasir')
driver.find_element(By.XPATH,"//input[@data-qa= 'email']").send_keys('salman@salman.com')
driver.find_element(By.XPATH,"//input[@data-qa= 'subject']").send_keys('Serious Matter')
driver.find_element(By.XPATH,"//input[@data-qa= 'name']").send_keys('Salman Nasir')
driver.find_element(By.XPATH,"//textarea[@data-qa= 'message']").send_keys('Salman Nasir is a very punctual guy.')
driver.find_element(By.XPATH,"//input[@type= 'file']").send_keys(os.path.abspath(os.path.join(r"C:\Users\HP\OneDrive\Desktop\python",r"salman.txt")))
driver.find_element(By.XPATH,"//input[@data-qa= 'submit-button']").click()
time.sleep(2)
driver.switch_to.alert.accept()







time.sleep(1000)