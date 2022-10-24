from selenium.webdriver.common.by import By
from selenium import webdriver

driver=r"C:\\Users\\1\\Desktop\\Efrat 2022\\VIA\\chromedriver.exe"
url="https://www.demoblaze.com"

driver = webdriver.Chrome(driver)
driver.get(url)

user_name="Efrat"
password="1234"