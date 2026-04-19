from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import re
import json
from datetime import datetime
import time
import pandas as pd

from src.transform import transformar_dados

def obter_cotacoes():
    driver = webdriver.Chrome()

    driver.get("https://www.cnabrasil.org.br/servicos/precos-commodities")

    time.sleep(5)
    
    tabela = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.commodities-table"))
    )

    linhas = tabela.find_elements(By.TAG_NAME, "tr")

    dados_brutos = []

    for linha in linhas:

        colunas = linha.find_elements(By.TAG_NAME, "td")

        dados = [c.text for c in colunas]

        if len(dados) > 0:
            dados_brutos.append(dados)

    driver.quit()

    print(f"Dados brutos extraidos: {len(dados_brutos)} linhas")

    dados_tratados = []

    for linha in dados_brutos:
        try:
            dado = transformar_dados(linha)

            if dado:
                dados_tratados.append(dado)

        except Exception as e:
            pass
    
    print(f"Dados tratados: {len(dados_tratados)} linhas")

    json_final = json.dumps(dados_tratados, indent=4, ensure_ascii=False)

    dados_tratados = json.loads(json_final)
    
    df_cotacoes = pd.DataFrame(dados_tratados)

    df_cotacoes.head(5)

    df_cotacoes["data"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df_cotacoes["data"] = pd.to_datetime(df_cotacoes["data"])
    df_cotacoes.head(5)
    return df_cotacoes