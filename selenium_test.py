from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

options.binary_location = "/usr/bin/chromium"

options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(
    service=service,
    options=options
)

driver.get("http://localhost:5000")

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")

driver.find_element(By.ID, "login").click()

print("Login test successful")

driver.quit()