# Mai jos este scriptul gata de a fi rulat,
# nu doar ce a generat functia "Record & Play"
# din Appium Inspector.

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Configurare conexiune:
DEVICE_IP_PORT = '192.168.1.5:35307'
APPIUM_SERVER_URL = 'http://127.0.0.1:4723'

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = DEVICE_IP_PORT
options.app_package = 'com.sec.android.app.popupcalculator'
options.app_activity = 'com.sec.android.app.popupcalculator.Calculator'
options.no_reset = True

print("Pornim aplicatia calculator...")
driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)

try:
    print("Asteptam deschiderea aplicatiei...")
    time.sleep(3)

    # Executam operatia aritmetica: 8 + 2 = 10
    print("Apasam pe 8...")
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="8")
    el1.click()
    
    print("Apasam pe Plus...")
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Plus")
    el2.click()
    
    print("Apasam pe 2...")
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="2")
    el3.click()
    
    print("Apasam pe Egal...")
    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Egal")
    el4.click()

    print("Operatie finalizata cu succes!")
    time.sleep(2) # Pauza pentru a putea vedea rezultatul pe ecran

finally:
    driver.quit()
    print("Sesiune Appium inchisa.")