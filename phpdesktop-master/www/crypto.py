import pymysql.cursors # try python3 -m pip install PyMySQL , 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import os
import json
import array

#connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='',
#                             database='smartmirror',
#                             cursorclass=pymysql.cursors.DictCursor)

PATH = "C:\Program Files (x86)\chromedriver.exe"

ob = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome(PATH)


url = "https://www.valuta.nl/cryptomunten"
driver.get(url)
time.sleep(1)

#pak de feestdagen
js_string = "var element = document.getElementById(\"gdpr-consent-tool-wrapper\");element.remove();"
driver.execute_script(js_string)
#make array readable
feestdagenExport = []
feestdagenExport.append(" array (")

#Create the php array with information from the website
feestdagCount = 1
divCounter = 1
for x in range(6):
    feestdag = driver.find_element_by_xpath("/html/body/form/div[3]/div/div[3]/div/div[1]/ul[2]/li["+ str(feestdagCount) +"]/a/div[1]")
    print (feestdag.text)
    feestdagenExport.append("\t"+ str(divCounter) +" => array (")

    feestdagenExport.append("\t\t'naam' => '"+ driver.find_element_by_xpath("/html/body/form/div[3]/div/div[3]/div/div[1]/ul[2]/li["+str(divCounter)+"]/a/div[1]").text + "',")
    feestdagCount += 1
    divCounter += 1
    feestdagenExport.append("\t\t'desc' => '"+ driver.find_element_by_xpath("/html/body/form/div[3]/div/div[3]/div/div[1]/ul[2]/li["+str(divCounter)+"]/a/div[2]").text + "',")
    feestdagenExport.append("\t),")


with open("cryptoExport.php", "w") as txt_file:
    txt_file.write("<?php\n $cryptoArray = ")
    for line in feestdagenExport:
        txt_file.write("".join(line) + "\n")
    txt_file.write(" )\n?>")
    txt_file.close()
print(feestdagenExport)

time.sleep(200)
driver.quit()