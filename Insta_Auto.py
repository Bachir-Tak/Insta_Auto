# Import

from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Firefox()
# Going to Instagram's website

driver.get("https://www.instagram.com/")
sleep(1)

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
elem.send_keys(Keys.RETURN)
sleep(7)

#Removal of additional pop-ups
if ("onetap" in driver.current_url) : 
    sleep(1)
    action_chains = ActionChains(driver)
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
    action_chains.click(elem).perform()    
    sleep(5)
if (EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]"))) :
    elem=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
    action_chains.click(elem).perform()    
    sleep(5)

#Closing 

assert "No results found." not in driver.page_source
driver.close()
