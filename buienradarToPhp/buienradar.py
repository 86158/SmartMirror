from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



# open browser
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# visit buienradar in browser
print("Enter buienradar")
driver.get("https://www.buienradar.nl/")
# confirm cookies and cancel location
driver.find_element_by_id("onetrust-accept-btn-handler").click()
print("cookies confirmed")
driver.find_element_by_link_text("Is goed, toon de popup").click()
print("location accepted")
time.sleep(1)

weersverwachting3Dagen = driver.find_elements_by_xpath("/html/body/div[2]/div/main/div[1]/div[1]/section[2]/div[1]/div/div[1]/div[1]/div[1]/div/table/tbody/tr")
print(weersverwachting3Dagen.text)

#make array readable
weersverwachtingexport = []
weersverwachtingexport.append("array (")

#Create the php array with information from the website
arrayCounter = 0
for day in weersverwachting3Dagen:
    print(day.text)
    weersverwachtingexport.append("\t"+ str(arrayCounter) +" => '" + str.replace(day.text, "°", "&deg;") + "',")
    arrayCounter += 1


with open("weersVerwachtingexport.php", "w") as txt_file:
    txt_file.write("<?php\n $weersVerwachtingArray = ")
    for line in weersverwachtingexport:
        txt_file.write("".join(line) + "\n")
    txt_file.write(")\n?>")
    txt_file.close()
driver.close()