from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

school = "ROC Ter AA"
schoolID = ""
gebruikersEMAIL = "stedentemail"
gebruikersNAAM = "studennummer"
wachtwoord = "wachtworst"

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://login.educus.nl/") 
print(driver.title)
search = driver.find_element_by_id("txtScholenZoekVeld")
search.send_keys(school)

time.sleep(1)

schoolID = driver.find_element_by_link_text(school)
print("selected school: " + schoolID.text)
schoolID.click()

time.sleep(1)

print(driver.title)
if driver.title == "Sign in to your account" : 
    emailMicrosoft = driver.find_element_by_id("i0116")
    emailMicrosoft.send_keys(gebruikersEMAIL)
    time.sleep(0.1)
    emailMicrosoftNext = driver.find_element_by_id("idSIButton9")
    emailMicrosoftNext.click()
    time.sleep(1.7)
    passwordMicrosoft = driver.find_element_by_id("i0118")
    passwordMicrosoft.send_keys(wachtwoord)
    passwordMicrosoftNext = driver.find_element_by_id("idSIButton9")
    passwordMicrosoftNext.click()
    time.sleep(1.5)
    emailMicrosoftNext = driver.find_element_by_id("idSIButton9")
    emailMicrosoftNext.click()
    time.sleep(2.5)
    
    navKnop = driver.find_element_by_id("id3")
    navKnop.click()
    agendaLink = driver.get("https://teraa-student.educus.nl/agenda")

    
