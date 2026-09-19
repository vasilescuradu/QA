# Testare Automată Appium - Aplicația Calculator

Acest proiect conține scripturi pentru automatizarea aplicației native Calculator folosind Appium.

## Descrierea Fișierelor

* **`script_appium_inspector.py`**
  Conține rezultatul creat de funcționalitatea “Record & Play”.

* **`script_complet.py`**
  Conține un script care poate fi rulat pentru a deschide aplicația calculator și a realiza calculul `8+2=10`. 
  *Notă:* În variabilele `app_package` și `app_activity` sunt puse denumiri specifice aplicației de calculator de pe telefoanele Samsung.

## Note privind identificarea elementelor UI

Aplicația calculator este o aplicație nativă Android. Acest lucru înseamnă că elementele de interfață expun atribute standard în ierarhia nativă a sistemului de operare – **View Hierarchy** –, putând fi citite de Appium prin UIAutomator.

**Portabilitate:** Acest script e portabil. Funcționează indiferent de ecranul dispozitivului, deoarece căutarea elementelor nu se face după coordonate de pixeli, ci direct prin interacțiunea cu elementele native din interfață.