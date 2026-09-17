# Mai jos e script-ul facut cu functia "Record & Play" din Appium Inspector.
# Calculul a fost: 8+2=10


el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="8")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Plus")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="2")
el3.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Egal")
el4.click()

