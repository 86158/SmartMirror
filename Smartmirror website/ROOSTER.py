from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.common.keys import Keys
import time

from PIL import Image
import PIL.ImageOps    


school = "ROC Ter AA"
schoolID = ""
gebruikersEMAIL = "86513@roc-teraa.nl"
gebruikersNAAM = "86513"
wachtwoord = "SnC6e6px"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/bin/chromedriver',)
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
    time.sleep(1) 
    emailMicrosoft = driver.find_element_by_id("i0116")
    emailMicrosoft.send_keys(gebruikersEMAIL)
    print('Filled in Email')
    
    time.sleep(0.1)
    emailMicrosoftNext = driver.find_element_by_id("idSIButton9")
    emailMicrosoftNext.click()
    time.sleep(1.7)
    passwordMicrosoft = driver.find_element_by_id("i0118")
    passwordMicrosoft.send_keys(wachtwoord)
    print('Filled in Password')
    
    passwordMicrosoftNext = driver.find_element_by_id("idSIButton9")
    passwordMicrosoftNext.click()
    time.sleep(1.5)
    emailMicrosoftNext = driver.find_element_by_id("idSIButton9")
    emailMicrosoftNext.click()
    time.sleep(2.5)
    agendaLink = driver.get("https://teraa-student.educus.nl/agenda")
    time.sleep(1.5)
    
    ele=driver.find_element("xpath", '//div[@class="agenda"]')
    total_height = ele.size["height"]+1000
    driver.set_window_size(1020, total_height)    
    print('Taking screenshot')
    ob=Screenshot_Clipping.Screenshot()
    element=driver.find_element_by_class_name('agenda')
    img_url=ob.get_element(driver, element, r'.')
    print(img_url + "INVERTING cOL0RZ NOW")
    image = Image.open(img_url)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('/home/pi/MagicMirror/modules/MMM-EasyPix/pix/rooster.png')
    print("now taking screenshot of results")
    agendaLink = driver.get("https://teraa-student.educus.nl/resultaten")
    time.sleep(2.0)
    ele=driver.find_element_by_class_name("result-overview--table") 
    print('Taking screenshot')
    element=driver.find_element_by_class_name('result-overview--table')
    imgs_url=ob.get_element(driver, element, r'.')
    print(imgs_url)
    image = Image.open(imgs_url)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('/home/pi/MagicMirror/modules/MMM-EasyPix/pix/cijfers.png')
    print("DONE! Starting the Mirror!")