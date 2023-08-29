import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Meu objeto de analise e pesquisa
vagas = {'desenvolvedor%20front%20end','desenvolvedor%20back%20end', 'banco%20de%20dados', 'analista%20de%20dados',
         'devops'}
info_vagas = {'empresa':[],'cargo':[], 'modalidade':[], 'cidade':[]}

for vaga in vagas:

    url = f'https://portal.gupy.io/job-search/term={vaga}'

    # Inicializar o navegador Chrome usando o Selenium
    driver = webdriver.Chrome()
    driver.get(url)

    # Rolagem até o fim da página, visando carregar to/do conteúdo
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

    infos = soup.find_all('div', class_=re.compile('dgHpeN'))

    for info in infos:
        empresa = info.find('p', class_=re.compile('cQyvth')).get_text().strip()
        cargo = info.find('h2', class_=re.compile('XNNQ')).get_text().strip()

        spans = info.find_all('span', class_=re.compile('cezNaf'))

        # Verificar se há pelo menos dois spans (modalidade e cidade)
        if len(spans) >= 2:
            cidade = spans[0].get_text().strip()
            modalidade = spans[1].get_text().strip()

        info_vagas['empresa'].append(empresa)
        info_vagas['cargo'].append(cargo)
        info_vagas['modalidade'].append(modalidade)
        info_vagas['cidade'].append(cidade)

#Por opcao vou salvar todas, no mesmo arquivo
df = pd.DataFrame(info_vagas)
df.to_csv(f'C:/Users/User/PycharmProjects/webscraping/vagas_abertas.csv', encoding='utf-8', sep=',')

