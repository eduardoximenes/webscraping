import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://portal.gupy.io/job-search/term=enfermeiro'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

driver = webdriver.Chrome()
driver.get('url')
while True:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    sleep(1)
    if driver.execute_script("return window.scrollY + window.innerHeight >= document.documentElement.scrollHeight"):
        break

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

dic_produtos = {'Empresa':[],'Cargo':[], 'Tipo de vaga':[], 'Modalidade':[], 'Cidade':[] }
produtos = soup.find_all('div', class_=re.compile('dgHpeN'))

    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()

        print(marca, preco)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

df = pd.DataFrame(dic_produtos)
df.to_csv('seu/path/preco_cadeira.csv', encoding='utf-8', sep=';')



driver.quit()

#infos que eu quero
# Empresa,	Cargo da vaga,	Tipo de vaga, Modalidade de trabalho,	Cidade