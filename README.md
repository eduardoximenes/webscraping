# webscraping
Web scraping de vagas de emprego abertas e análise sobre os dados.

A página escolhida para fazer o scrapping foi o https://portal.gupy.io/, foi necessário salvar uma lista com termos de pesquisa para buscar cada uma das vagas desejadas. Utilizei a biblioteca Selenium para automtizar a tarefa de rolar até o fim da página para que pudesse carregar todas as vagas. Após isso bastou extrair os dados de cada div - com a biblioteca BeautifulSoup - armazenar em uma matriz e salvar estes dados em formato .csv.

Por fim, ao carregar o arquivo .csv no excel e usar as ferramentas de tabela dinâmica, criei alguns filtros e gráficos responsivos para as informações que buscavamos, salvando por fim em um .xlsx.


