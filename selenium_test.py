from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor="http://selenium-chrome:4444",
    options=options
)

driver.get("http://myapp-container:5000")

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")

driver.find_element(By.ID, "login").click()

print("Test completed")

driver.quit()