import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

url = 'https://portal.gupy.io/job-search/term=enfermeiro'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/116.0.0.0 Safari/537.36"}

# Inicializar o navegador Chrome usando o Selenium
driver = webdriver.Chrome()
driver.get(url)

# Rolar até o final da página repetidamente
while True:
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)
    sleep(0.5)
    if driver.execute_script("return window.scrollY + window.innerHeight >= document.documentElement.scrollHeight"):
        break

# Obter o conteúdo da página após rolar até o final
page_content = driver.page_source
driver.quit()

# Usar BeautifulSoup para analisar o conteúdo da página
soup = BeautifulSoup(page_content, 'html.parser')

#, 'tipo de vaga':[], 'modalidade':[], 'cidade':[]
dic_produtos = {'empresa':[],'cargo':[]}
produtos = soup.find_all('div', class_=re.compile('dgHpeN'))

for produto in produtos:
    empresa = produto.find('p', class_=re.compile('cQyvth')).get_text().strip()
    cargo = produto.find('h2', class_=re.compile('XNNQ')).get_text().strip()
    dic_produtos['empresa'].append(empresa)
    dic_produtos['cargo'].append(cargo)
    #print(empresa, cargo)

df = pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/User/PycharmProjects/vagas.csv', encoding='utf-8', sep=',')
