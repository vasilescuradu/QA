# Automatizare Magazin Play - Hill Climb Racing

In acest folder se afla scriptul `script_cerinta_2.py`, creat pentru a interacționa automatizat cu aplicația Magazin Play (Google Play Store).

## Funcționalitate principală
Scriptul `script_cerinta_2.py` deschide aplicația Magazin Play, caută jocul **Hill Climb Racing**, inițiază instalarea acestuia și, după finalizare, îl deschide.

## Gestionarea elementelor dinamice
Timpul de descărcare și instalare a unei aplicații este impredictibil, fiind influențat de viteza rețelei și de dimensiunea pachetului APK. În timpul acestui proces, butonul principal al interfeței își schimbă starea secvențial:
1. **„Instalați”**
2. **„Anulează”** (în timpul descărcării/instalării)
3. **„Joacă”** (după finalizarea instalării)

Am gestionat aceste schimbări de stare utilizând **explicit waits** (așteptări explicite) prin clasa `WebDriverWait`. Regula de așteptare este dinamică: framework-ul monitorizează ecranul și așteaptă apariția butonului „Joacă” pentru un interval de maxim **180 de secunde**. Imediat după ce apare butonul, scriptul acționează, ceea ce face ca implementarea să fie eficientă. 

*Notă privind timeout-ul:* Am setat timeout-ul la 180s deoarece am observat, prin încercări practice, că acest interval este suficient - în general, jocul se descarcă și se instalează între 2 și 3 minute.

## Dependențe de limbă
Aplicația Magazin Play de pe telefonul de test este setată în limba română. Din acest motiv, **acest script funcționează doar pentru interfața în limba română**. A fost necesar să caut exact denumirile butoanelor și să le scriu explicit în cod, iar aceste denumiri ("Instalați", "Joacă") au fost în română.

## Instrumente utilizate și strategii de localizare UI
* **Appium Inspector:** Am avut nevoie de Appium Inspector pentru a analiza ierarhia aplicației și a stabili exact pe ce elemente de UI trebuie să dau click.
* **Sugestii AI pentru selectoare:** Am folosit asistență AI pentru anumite sugestii de localizare - locators. De exemplu, printre rezultatele căutării, îmi apărea și jocul *Hill Climb Racing 2*. Pentru a găsi o modalitate de a-l evita, am creat o regulă specifică: am căutat un element care începe cu „Hill Climb Racing” și **nu conține** cifra „2”.
