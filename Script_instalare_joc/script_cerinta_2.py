from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurare conexiune:
DEVICE_IP_PORT = '192.168.1.5:43257'
APPIUM_SERVER_URL = 'http://127.0.0.1:4723'
TARGET_PACKAGE = 'com.fingersoft.hillclimb' # Joc mic pt. descarcare rapida

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = DEVICE_IP_PORT
options.no_reset = True

driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
# Initializam obiectul WebDriverWait cu o limita de 180 s
wait = WebDriverWait(driver, 180) 

try:
    driver.activate_app('com.android.vending')
    print("Asteptam sa se incarce Magazin Play...")

    time.sleep(3) # Asteptam 3 secunde ca sa fim siguri ca s-a incarcat complet interfata

    # Asteptam explicit pana cand bara de search este vizibila si gata de click
    search_bar = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='Caută']")))
    search_bar.click()

    search_bar_2 = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='Caută aplicații și jocuri']")))
    search_bar_2.click()
    
    # Cautam dupa package name
    print(f"Cautam jocul dupa package name: {TARGET_PACKAGE}...")
    search_input = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
    search_input.send_keys(TARGET_PACKAGE)
    
    # Apasam tasta enter de pe tastatura telefonului - keycode 66
    driver.press_keycode(66)

    xpath_card = "//android.view.View[starts-with(@content-desc, 'Hill Climb Racing') and not(contains(@content-desc, '2'))]"
    app_card = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath_card)))
    app_card.click()

    print("Asteptam butonul de instalare...")
    # Asteptam sa apara butonul de instalare si dam click
    install_btn = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='Instalați']")))
    install_btn.click()
    
    print("Se descarca jocul. Asteptam aparitia butonului play...")
    # Scriptul va sta pe loc - maxim 180 s - pana cand butonul 'Instalați' se transforma in 'Joacă'
    play_btn = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//*[@text='Joacă']")))
    
    print("Jocul s-a instalat! Lansam jocul...")
    play_btn.click()
    
    # Lasam jocul deschis putin pt. verificare
    time.sleep(5)
    print("Test finalizat cu succes!")

finally:
    driver.quit()