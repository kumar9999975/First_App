from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:5000")

# Username
driver.find_element(By.NAME, "username").send_keys("admin")

# Password
driver.find_element(By.NAME, "password").send_keys("admin")

# Login button
driver.find_element(By.ID, "login").click()

driver.quit()