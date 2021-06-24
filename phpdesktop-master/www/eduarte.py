from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# login settings
eduarteSchool   = "ROC Ter AA"
eduarteMail     = "86513@roc-teraa.nl"
eduarteUsername = "86513"
eduartePassword = "SnC6e"

# open browser
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

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

# next part
# visit eduarte in browser
print("Enter School")
driver.get("https://login.educus.nl/")
driver.find_element_by_id("txtScholenZoekVeld").send_keys(eduarteSchool)
# confirm school
print("Select School")
driver.find_element_by_link_text(eduarteSchool).click()

time.sleep(2.5)

# login microsoftonline
if driver.title == "Sign in to your account" :
    print("Enter school Mail adress")
    driver.find_element_by_id("i0116").send_keys(eduarteMail)
    driver.find_element_by_id("idSIButton9").click()
    print("Enter school password")
    driver.find_element_by_id("i0118").send_keys(eduartePassword)
    time.sleep(2)

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
imgs_url=ob.get_element(driver, element, save_location=r"C:\xampp\htdocs\Smartmirror\images")
print(imgs_url)
if os.path.isfile(r'images\cijfers.png') == True:
    os.remove(r'images\cijfers.png')
    print('Deleted residu file')
if os.path.isfile(r'images\clipping_shot.png') == True:
    os.remove(r'images\clipping_shot.png')
    print('Deleted old clippingshot')
os.rename(imgs_url,r'images\cijfers.png')
print('Renamed the results file')
mirrorwebsite = driver.get('http://localhost/Smartmirror')

#close browser after 1 second