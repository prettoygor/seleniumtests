import os
from lib2to3.pgen2 import driver
from telnetlib import EC
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"D:/workspace/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('https://www.calculadora-online.xyz/calculadora-horario.php')

print("Maximizing window")
driver.maximize_window()

driver.implicitly_wait(15)

#Fields
firsthour = driver.find_element(By.ID,"heure1")
secondhour = driver.find_element(By.ID,"heure2")
firstmin = driver.find_element(By.ID,"min1")
secondmin = driver.find_element(By.ID,"min2")
firstsec = driver.find_element(By.ID,"sec1")
secondsec = driver.find_element(By.ID,"sec2")

#Buttons
addition = driver.find_element(By.ID,"addition_time")
subtraction = driver.find_element(By.ID,"soustraction_time")
reset = driver.find_element(By.ID,"reset_time")

#Checkbox
keep_checkbox = driver.find_element(By.ID,"retenu_auto")

#Usando o método "send_keys" para enviar os valores desejados para os campos. Esse método pode também enviar teclas como "Shift", "CTRL" e etc, basta importar o "from selenium.webdriver.common.keys import Keys"
firsthour.send_keys(1)
secondhour.send_keys(4)
firstmin.send_keys(Keys.NUMPAD5, Keys.NUMPAD0)

addition.click()
keep_checkbox.click()

test = driver.find_element(By.ID,"asdfasdf")

