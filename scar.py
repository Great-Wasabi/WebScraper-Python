import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chromedriver = "/chromedriver"
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser"
s = Service(chromedriver)

driver = webdriver.Chrome(service=s, options=options)

driver.get("http://quotes.toscrape.com/")

driver.find_element(By.LINK_TEXT, "Login").click()
time.sleep(3)
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("admin")
password.send_keys("1234")
driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

file = open("quotes.csv", "w")
writer = csv.writer(file)
writer.writerow(["Quote", "Author"])
for quote, author in zip(quotes, authors):
    writer.writerow([quote.text, author.text])
file.close()
