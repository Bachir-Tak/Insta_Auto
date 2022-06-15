# Import

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()

# Going to Instagram's website

driver.get("https://www.instagram.com/")
sleep(2)

# Reading credentials in text file

f = open("Credentials", "r")
email=f.readline()
mdp=f.readline()

# Entering Credentials and connecting

elem = driver.find_element(By.NAME, "username")
elem.clear()
elem.send_keys(email)
elem = driver.find_element(By.NAME,"password")
elem.clear()
elem.send_keys(mdp)
sleep(1)
elem.send_keys(Keys.RETURN)
sleep(7)

#Closing 
assert "No results found." not in driver.page_source
driver.close()