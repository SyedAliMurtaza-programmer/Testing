from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

a = webdriver.ChromeOptions()
a.add_argument('--start-maximized')
driver = webdriver.Chrome(options=a)

driver.get("https://automationexercise.com/")
driver.find_element(By.CSS_SELECTOR,"a[href='/login']").click()
driver.find_element(By.XPATH,"//input[@data-qa = 'signup-name']").send_keys("ali")
driver.find_element(By.XPATH,"//input[@data-qa = 'signup-email']").send_keys("sajid112@hotmail.com")
driver.find_element(By.XPATH,"//button[@data-qa = 'signup-button']").click()
driver.find_element(By.XPATH,"//div[@id = 'uniform-id_gender1']").click()
driver.find_element(By.XPATH,"//input[@id = 'password']").send_keys("Password")
days = Select(driver.find_element(By.XPATH,"//select[@id = 'days']"))
days.select_by_value("20")
months = Select(driver.find_element(By.XPATH,"//select[@id = 'months']"))
months.select_by_value("9")
year = Select(driver.find_element(By.XPATH,"//select[@id = 'years']"))
year.select_by_value("1999")
driver.find_element(By.XPATH,"//input[@id = 'newsletter']").click()
driver.find_element(By.XPATH,"//input[@data-qa = 'first_name']").send_keys("Sajid")
driver.find_element(By.XPATH,"//input[@data-qa = 'last_name']").send_keys("Mehmood")
driver.find_element(By.XPATH,"//input[@data-qa = 'company']").send_keys("SajidSchools")
driver.find_element(By.XPATH,"//input[@data-qa = 'address']").send_keys("10 Brookdale Drive,Armadale")
country = Select(driver.find_element(By.XPATH,"//select[@data-qa = 'country']"))
country.select_by_value("Australia")
driver.find_element(By.XPATH,"//input[@data-qa = 'state']").send_keys("WA")
driver.find_element(By.XPATH,"//input[@data-qa = 'city']").send_keys("Perth")
driver.find_element(By.XPATH,"//input[@data-qa = 'zipcode']").send_keys("6110")
driver.find_element(By.XPATH,"//input[@data-qa = 'mobile_number']").send_keys("123456789")

driver.find_element(By.XPATH,"//button[@data-qa = 'create-account']").click()
time.sleep(1000)
print("Account created")

