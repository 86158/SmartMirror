from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import subprocess


# login settings
eduarteSchool   = "ROC Ter AA"
eduarteMail     = "86513@roc-teraa.nl"
eduarteUsername = "86513"
eduartePassword = "SnC6e6px"

# open browser
PATH = "C:\Program Files (x86)\chromedriver.exe"
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
for x in range(8):
    feestdag = driver.find_element_by_xpath("/html/body/form/div[3]/div/div[3]/div/div[1]/ul[2]/li["+ str(feestdagCount) +"]/a/div[1]")
    print (feestdag.text)
    feestdagenExport.append("\t"+ str(divCounter) +" => array (")

    feestdagenExport.append("\t\t'naam' => '"+ driver.find_element_by_xpath("/html/body/form/div[3]/div/div[3]/div/div[1]/ul[2]/li["+str(divCounter)+"]/a/div[1]").text + "',")
    feestdagCount += 1

    feestdagenExport.append("\t\t'desc' => '"+ driver.find_element_by_xpath("/html/body/form/div[3]/div/div[3]/div/div[1]/ul[2]/li["+str(divCounter)+"]/a/div[2]").text + "',")
    feestdagenExport.append("\t),")
    divCounter += 1

with open("cryptoExport.php", "w") as txt_file:
    txt_file.write("<?php\n $cryptoArray = ")
    for line in feestdagenExport:
        txt_file.write("".join(line) + "\n")
    txt_file.write(" )\n?>")
    txt_file.close()
print(feestdagenExport)


#visit specialdays for the recent feestdagen
url = "https://www.iagenda.com/nl/home/specialdays"
driver.get(url)
time.sleep(1)
count = 1
#pak de feestdagen
feestdagen = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[1]/table/tbody/li[4]")
#make array readable
feestdagenExport = []
feestdagenExport.append(" array (")

#Create the php array with information from the website
feestdagCount = 2
for x in range(4):
    feestdag = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/table/tbody/tr[" + str(feestdagCount) + "]")
    print (feestdag.text)
    feestdagenExport.append("\t"+ str(feestdagCount - 2) +" => array (")
    feestdagCount += 1
    feestdagenExport.append("\t\t'datum' => '"+ driver.find_element_by_xpath("/html/body/div[5]/div/div/table/tbody/tr["+ str(feestdagCount) +"]/td[2]").text + "',")
    feestdagenExport.append("\t\t'desc' => '"+ driver.find_element_by_xpath("/html/body/div[5]/div/div/table/tbody/tr["+ str(feestdagCount) +"]/td[3]").text + "',")
    feestdagenExport.append("\t),")

#Save the array in a php file so the mirror can read it
with open("feestdagExport.php", "w") as txt_file:
    txt_file.write("<?php\n $feestdagenArray = ")
    for line in feestdagenExport:
        txt_file.write("".join(line) + "\n")
    txt_file.write(" )\n?>")
    txt_file.close()
print(feestdagenExport)

# visit buienradar in browser
print("Enter buienradar")
driver.get("https://www.buienradar.nl/")
time.sleep(2)
# confirm cookies and cancel location
driver.find_element_by_id("onetrust-accept-btn-handler").click()
print("cookies confirmed")
driver.find_element_by_link_text("Is goed, toon de popup").click()
print("location accepted")
time.sleep(1)

weersverwachting3Dagen = driver.find_elements_by_xpath("/html/body/div[2]/div/main/div[1]/div[1]/section[2]/div[1]/div/div[1]/div[1]/div[1]/div/table/tbody/tr")
print(weersverwachting3Dagen)

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
time.sleep(1)
# visit eduarte in browser
print("Enter School")
driver.get("https://login.educus.nl/")
driver.find_element_by_id("txtScholenZoekVeld").send_keys(eduarteSchool)
# confirm school
time.sleep(1)
print("Select School")
driver.find_element_by_link_text(eduarteSchool).click()

time.sleep(3)

# login microsoftonline

print("Enter school Mail adress")
driver.find_element_by_id("i0116").send_keys(eduarteMail)
driver.find_element_by_id("idSIButton9").click()
time.sleep(2)
print("Enter school password")
driver.find_element_by_id("i0118").send_keys(eduartePassword)
time.sleep(1)

print("Login")
driver.find_element_by_id("idSIButton9").click()

print("Save login")
driver.find_element_by_id("idSIButton9").click()

#next part
# open agenda
print("Open agenda")
driver.get("https://teraa-student.educus.nl/agenda")
time.sleep(1)
print("lijst weergaven")
driver.find_element_by_xpath("/html/body/div[1]/div/section/div[2]/div[1]/div/div[3]/div/ul/li[1]/a").click()
time.sleep(1)

# Download Eduarte rooster
# Get days from list
eduarteRooster = driver.find_elements_by_class_name("agenda-title")

#make array that is readable for php
roosterExport = []
roosterExport.append("array (")

# integers:
dayNumber = 1
for roosterDag in eduarteRooster:
    # Current subject:
    vakNumber = 1
    # get all days in list
    roosterUur = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/section/div[2]/div[2]/div/table["+ str(dayNumber) +"]/tbody/tr")
    # print the date
    print(roosterDag.text)

    # export indexes
    roosterExportVakIndex = 0

    # put data in txt array
    roosterExport.append("\t"+ str(dayNumber -1) +" => array (")
    roosterExport.append("\t\t"+ "'day'" +" => '" + roosterDag.text + "',")
    roosterExport.append("\t\t"+ "'subjects'" +" => array (")

    for vakTable in roosterUur:
        # get classroom,subject,class and docent (all from the same place)
        roosterVak = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/section/div[2]/div[2]/div/table["+ str(dayNumber) +"]/tbody/tr["+ str(vakNumber) +"]/td[3]/span[1]")
        # Get start and end time of subject
        roosterBeginTijd = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/section/div[2]/div[2]/div/table["+ str(dayNumber) +"]/tbody/tr["+ str(vakNumber) +"]/td[2]/span[1]")
        roosterEindTijd = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/section/div[2]/div[2]/div/table["+ str(dayNumber) +"]/tbody/tr["+ str(vakNumber) +"]/td[2]/span[2]")
        # print subject information + times
        print(roosterVak[0].text + "    " + roosterBeginTijd[0].text + " - " + roosterEindTijd[0].text)
        # put subjects data in txt array
        
        roosterExport.append("\t\t\t"+ str(roosterExportVakIndex) +" => array (")
        roosterExport.append("\t\t\t\t"+ "'vak'" +" => '" + roosterVak[0].text +"',")
        roosterExport.append("\t\t\t\t"+ "'begintijd'" +" => '" + roosterBeginTijd[0].text +"',")
        roosterExport.append("\t\t\t\t"+ "'eindtijd'" +" => '" + roosterEindTijd[0].text +"',")
        roosterExport.append("\t\t\t),")

        
        roosterExportVakIndex += 1

        vakNumber += 1
    dayNumber += 1


    roosterExport.append("\t\t),")
    roosterExport.append("\t),")
roosterExport.append(")")

#save array as txt
with open("roosterExport.php", "w") as txt_file:
    txt_file.write("<?php\n $roosterArray = ")
    for line in roosterExport:
        txt_file.write("".join(line) + "\n")
    txt_file.write("?>")
    txt_file.close()
    
#go to results for screenshot
ob = Screenshot_Clipping.Screenshot()
agendaLink = driver.get("https://teraa-student.educus.nl/resultaten")
driver.set_window_size(750, 1020)
time.sleep(2.0)
selects = driver.find_elements_by_xpath("//span[@class='grade-structure--grade']")
for select in selects:
    script = 'document.styleSheets[0].insertRule(".result-overview--table>tbody>tr>td {background-color: black; color: white}", 0 )' 
    driver.execute_script(script)

#take screenshot of the results
ele=driver.find_element_by_class_name("result-overview--table") 
print('Taking screenshot')
element=driver.find_element_by_class_name('result-overview--table')
imgs_url=ob.get_element(driver, element, save_location=r"C:\Smartmirror\www\images")
print(imgs_url)
if os.path.isfile(r'C:\Smartmirror\www\images\cijfers.png') == True:
    os.remove(r'C:\Smartmirror\www\images\cijfers.png')
    print('Deleted residu file')
if os.path.isfile(r'C:\Smartmirror\www\images\clipping_shot.png') == True:
    os.remove(r'C:\Smartmirror\www\images\clipping_shot.png')
    print('Deleted old clippingshot')
os.rename(imgs_url,r'C:\Smartmirror\www\images\cijfers.png')
print('Renamed the results file')


subprocess.call([os.path.realpath(__file__) + "/../../phpdesktop-chrome.exe"])

#close browser after 1 second