"""
Am rezolvat cerinta 3 pe telefonul meu.

Am scris si un README cu imaginile din joc si cu mai multe detalii, in caz
ca e necesar.

Acest script lanseaza Asphalt 8 si navigheaza automat prin meniurile acestui joc.
Mai exact, din meniul principal intru pe setari, apoi pe info, apoi pe help, apoi pe
cele 7 butoane din help.
Deoarece Asphalt 8 este construit intr-un motor grafic custom, elementele de 
interfata - UI - nu expun atribute standard de Android.
Prin urmare, interactiunea cu butoanele din meniuri se bazeaza pe coordonate 
fixe X, Y, pe care le-am obtinut din Appium Inspector.

Probleme intampinate cu pop-up-uri si reclame dinamice:
- Uneori vin cate 2 reclame una dupa alta, alteori doar o singura reclama.
- Unele pop-up-uri se pot inchide cu X, altele necesita sa alegi "NOT NOW" sau
"CHECK IT"
- Modul in care se inchid reclamele variaza - unele au buton de X in stanga sus,
altele il au in dreapta sus, etc.

Delay am folosit dupa ce deschid jocul ca sa astept sa se incarce - trebuie un
delay suficient de mare - am pus 25 de secunde si a fost suficient, incarcarea terminandu-se
in general dupa 20 de secunde.
Am mai folosit delay-uri dupa ce apas butoane ca sa astept animatiile de trecere de la un
meniu la altul. Aici 2-3 secunde au fost suficiente.


Concluzie:

Coordonatele statice nu reusesc sa evite pop-up-uri diferite si reclame cu diverse
tipuri de confirmari necesare. Am citit si am inteles ca, pt. astfel de situatii,
se folosesc tehnici precum OCR sau Image Recognition. Despre OCR imi amintesc ca s-a
discutat si in cadrul workshop-ului.

Pt. situatiile in care nu apar pop-up-uri sau reclame, scriptul reuseste sa apese corect
toate butoanele pe telefonul meu - am testat de mai multe ori.
"""

from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

DEVICE_IP_PORT = '192.168.1.5:35655'
APPIUM_SERVER_URL = 'http://127.0.0.1:4723'

# 1. Coordonate meniul principal - Setari
COORD_SETARI_X = 2198
COORD_SETARI_Y = 83

# 2. Coordonate meniul setari - INFO
COORD_INFO_X = 747
COORD_INFO_Y = 747

# 3. Coordonate meniul info - HELP
COORD_HELP_X = 753
COORD_HELP_Y = 249

# 4. Coordonate sub-meniuri help
COORD_PARENT_INFO_X, COORD_PARENT_INFO_Y = 443, 255
COORD_GENERAL_X, COORD_GENERAL_Y = 421, 371
COORD_GAMEPLAY_X, COORD_GAMEPLAY_Y = 404, 487
COORD_TIME_EVENTS_X, COORD_TIME_EVENTS_Y = 426, 626
COORD_CONTROLS_X, COORD_CONTROLS_Y = 432, 731
COORD_OPTIONS_X, COORD_OPTIONS_Y = 404, 852
COORD_CUSTOMIZATION_X, COORD_CUSTOMIZATION_Y = 404, 974

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = DEVICE_IP_PORT
options.app_package = 'com.gameloft.android.ANMP.GloftA8HM'
options.app_activity = 'com.gameloft.android.ANMP.GloftA8HM.MainActivity'
options.no_reset = True

print("Pornim sesiunea Appium...")
driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)

try:
    # PASUL 1: Incarcarea jocului
    print("Asteptam 25s pentru incarcarea meniului principal...")
    time.sleep(25) 

    # PASUL 2: Navigarea spre meniul HELP
    print("Click pe 'Settings'...")
    driver.execute_script('mobile: clickGesture', {'x': COORD_SETARI_X, 'y': COORD_SETARI_Y})
    time.sleep(3) # Asteptam animatia de deschidere a meniului
    
    print("Click pe 'INFO'...")
    driver.execute_script('mobile: clickGesture', {'x': COORD_INFO_X, 'y': COORD_INFO_Y})
    time.sleep(2)
    
    print("Click pe 'HELP'...")
    driver.execute_script('mobile: clickGesture', {'x': COORD_HELP_X, 'y': COORD_HELP_Y})
    time.sleep(3) # Asteptam sa se incarce lista cu cele 7 categorii

    # PASUL 3: Iterarea prin cele 7 butoane din meniul help
    # Cream o lista cu toate butoanele pe care vrem sa le apasam succesiv
    help_menu_buttons = [
        {"name": "Parent info", "x": COORD_PARENT_INFO_X, "y": COORD_PARENT_INFO_Y},
        {"name": "General", "x": COORD_GENERAL_X, "y": COORD_GENERAL_Y},
        {"name": "Gameplay", "x": COORD_GAMEPLAY_X, "y": COORD_GAMEPLAY_Y},
        {"name": "Time-limited events", "x": COORD_TIME_EVENTS_X, "y": COORD_TIME_EVENTS_Y},
        {"name": "Controls", "x": COORD_CONTROLS_X, "y": COORD_CONTROLS_Y},
        {"name": "Options", "x": COORD_OPTIONS_X, "y": COORD_OPTIONS_Y},
        {"name": "Customization", "x": COORD_CUSTOMIZATION_X, "y": COORD_CUSTOMIZATION_Y}
    ]

    print("Incepem verificarea sub-meniurilor din help...")
    
    # Trecem prin fiecare buton din lista:
    for button in help_menu_buttons:
        print(f" -> Apasam pe categoria: {button['name']}")
        
        driver.execute_script('mobile: clickGesture', {
            'x': button['x'],
            'y': button['y']
        })
        
        # Asteptam 1.5 secunde intre click-uri ca sa se observe 
        # schimbarea textului din panoul din dreapta pe ecranul telefonului
        time.sleep(1.5) 

    print("Toate categoriile au fost accesate cu succes!")
    time.sleep(3) # Pauza finala

finally:
    driver.quit()
    print("Test finalizat.")