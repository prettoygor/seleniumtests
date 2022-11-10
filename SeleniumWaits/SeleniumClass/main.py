from lib2to3.pgen2 import driver
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Adiciona o caminho do navegador a variável, podendo ter múltiplos caminhos, por isso o "+="
os.environ['PATH'] += r"D:/workspace/SeleniumDrivers"

#Define o navergador usado para o teste.
print("Initiating Chrome driver")
driver = webdriver.Chrome()

#Define o site que será acessado ao abrir ao executar o código
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

#Aumenta o tamanho da tela.
print("Maximizing window")
driver.maximize_window()

#Define um tempo de espera entre cada ação, em segundos. Importante para evitar casos onde existe alguma lentidão, assim é aguardado o tempo e então a função é ececutada. Caso o elemento utilizado seja encontrado antes do tempo a ação é executada, não é necessário aguardar todo o tempo. Conhecida como espera implicita, pois irá realizar a ação assim que encontrar o elemento que foi definido.
driver.implicitly_wait(15)

#Define um elemento que deve ser encontrado na página, nesse caso um botão sendo encontrado pelo Id dele.
download_button = driver.find_element(By.ID,"downloadButton")

#Define a função que será executada pelo elemento, nesse caso ele será clicado
download_button.click()

#Define novamente um elemento, dessa vez por CLASS_NAME
download_progress = driver.find_element(By.CLASS_NAME, "progress-label")
#Printa o texto que está escrito no elemento, utilizando o NOME_DO_ELEMENTO.text, nesse caso irá apresentar o nome original do elemento, uma vez que ele começa com "Startging Download" e somente após finalizar vai para "Completed!"
print(f"{download_progress.text}")
#Verifica se o elemento é igual a "Completed!"
print(f"{download_progress.text == 'Complete!'}")

#Define um tempo de espera com uma condição, nesse caso serão 30 segundos, com uma condição esperada (EC) que valida que deve ser esperado até (until) que o elemento definido (CLASS_NAME) tenha o valor definido (Completed!) - Conhecida como espera EXPLICITA, pois é dada uma condição que será aguardada para depois prosseguir com a ação
WebDriverWait(driver, 30).until(
  EC.text_to_be_present_in_element(
    #Element filtration
    (By.CLASS_NAME, 'progress-label'),
    #The expected text
    'Complete!'
  )
)
print(f"{download_progress.text}")
print(f"{download_progress.text == 'Complete!'}")