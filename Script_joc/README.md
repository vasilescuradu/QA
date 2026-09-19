# Proiect Workshop QA - Cerința 3: Joc & Meniuri

Acest proiect reprezintă rezolvarea cerinței numărul 3 din tema workshop-ului de QA: *Lansează un joc, navighează prin meniuri (Settings/Profile/Help). Notează provocările cu elementele dinamice și delay-urile.*

## 1. Ce face scriptul

Scriptul automatizează interacțiunea cu jocul **Asphalt 8** și parcurge următorii pași:
1. Deschide jocul Asphalt 8.
2. Apasă pe butonul de **Settings**.
3. Apasă pe butonul de **Info**.
4. Apasă pe **Help**.
5. Apasă pe toate butoanele din meniul de "Help", de sus în jos (ex: *What's New, Tutorials, Customer Care, About, etc.*).

## 2. Provocări cu elementele dinamice

Scriptul funcționează conform așteptărilor într-un flux ideal, însă au fost identificate următoarele provocări generate de elemente dinamice (precum reclamele și pop-up-urile):
* **Reclame impredictibile:** Uneori apar două reclame consecutiv, alteori doar una. De asemenea, butonul de închidere (X) își schimbă constant poziția (uneori în stânga-sus, alteori în dreapta-sus).
* **Pop-up-uri inconsistente:** Structura pop-up-urilor diferă masiv (ex: notificările pentru "Car Hunt"). Unele se pot închide cu "X", în timp ce altele necesită selectarea unor opțiuni specifice din ecran, precum "NOT NOW" sau "CHECK IT".
* **Dependența de rezoluție (Coordonate Relative):** Folosirea coordonatelor fixe (valorile X și Y) pentru a da click înseamnă că scriptul funcționează corect doar pe ecranul dispozitivului curent. Pe alte telefoane cu rezoluții diferite, coordonatele nu se vor mai potrivi.

## 3. Gestionarea Delay-urilor

Pentru a asigura o rulare stabilă, au fost implementate următoarele pauze (delay-uri):
* **Încărcarea jocului:** Un delay de **25 de secunde** la pornirea inițială pentru a permite încărcarea completă a resurselor grele ale jocului.
* **Tranzițiile între meniuri:** Între apăsările de butoane s-a folosit un delay de **2-3 secunde**, timp suficient pentru a lăsa animațiile de tranziție ale interfeței să se finalizeze.

## 4. Detalii Setup și Configurare

Mediul de testare a fost configurat folosind un dispozitiv fizic cu **Android 12**.

### Verificare și Instalare Tool-uri
Mai jos se află configurația sistemului și versiunile instalate pentru suita Appium:

```powershell
PS C:\Users\username> npm -version
11.16.0
PS C:\Users\username> node -v
v24.18.1
PS C:\Users\username> appium -version
3.6.0
PS C:\Users\username> appium-doctor -version
1.16.2
PS C:\Users\username> appium driver list --installed
Listing installed drivers (rerun with --verbose for more info)
- uiautomator2@8.2.2 [installed (npm)]
- chromium@3.0.7 [installed (npm)]
PS C:\Users\username> pip show Appium-Python-Client
Name: Appium-Python-Client
Version: 5.3.1
Summary: Python client for Appium
Location: C:\Users\username\AppData\Local\...
PS C:\Users\username> adb version
Android Debug Bridge version 1.0.41
Version 37.0.1-15733141
Installed as C:\Users\username\AppData\Local\Android\Sdk\platform-tools\adb.exe
PS C:\Users\username> appium plugin list --installed
Listing installed plugins (rerun with --verbose for more info)
- inspector@2026.7.1 [installed (npm)]
```

### Conectarea ADB prin Wi-Fi (Wireless Debugging)
Deoarece nu a fost disponibil un cablu USB, dispozitivul a fost conectat prin rețeaua Wi-Fi locală. 
1. S-au activat **Opțiunile pentru dezvoltatori**.
2. S-a activat **Remedierea erorilor wireless (Wireless Debugging)**.
3. S-a realizat asocierea (pairing) utilizând codul de 6 cifre, urmată de conectarea la portul de depanare:

```powershell
PS C:\Users\username> adb pair 192.168.1.5:36033
Enter pairing code: 207640
* daemon not running; starting now at tcp:5037
* daemon started successfully
Successfully paired to 192.168.1.5:36033 [guid=adb-R58R54D6BTJ-CaSkEX]

PS C:\Users\username> adb connect 192.168.1.5:35655
connected to 192.168.1.5:35655

PS C:\Users\username> adb devices
List of devices attached
192.168.1.5:35655      device
```

### Pornire Appium Server
Serverul Appium a fost pornit incluzând plugin-ul de Inspector:

```powershell
PS C:\Users\username> appium --use-plugins=inspector
[Appium] Attempting to load plugin inspector...
[Appium] AppiumInspectorPlugin has been successfully loaded
[Appium] Welcome to Appium v3.6.0
[Appium] Appium REST http interface listener started on http://0.0.0.0:4723
```

### Capabilități Appium (Desired Capabilities)
În script și în Appium Inspector s-au folosit următoarele capabilități pentru atașarea la sesiune:

```json
{
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:deviceName": "192.168.1.5:35655",
  "appium:appPackage": "com.gameloft.android.ANMP.GloftA8HM",
  "appium:appActivity": "com.gameloft.android.ANMP.GloftA8HM.MainActivity",
  "appium:noReset": true
}
```