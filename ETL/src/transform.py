import re
import json
from datetime import datetime

import pandas as pd

def transformar_dados(linha):

    produto_info = linha[0]
    preco_info = linha[3]

    parte1 = produto_info.split("\n")

    produto = parte1[0].capitalize()

    uf_praca = parte1[1].split("/")
    uf = uf_praca[0].strip()
    praca = uf_praca[1].strip().capitalize()

    preco_linha = preco_info.split("\n")[0]

    preco_match = re.search(
    r'R\$\s*([\d.,]+)',
    preco_linha
    )

    preco_str = preco_match.group(1)

    preco = float(
        preco_str
        .replace(".", "")
        .replace(",", ".")
    )

    variacao = re.search(r'\(([\d,]+)', preco_linha).group(1)
    variacao = float(variacao.replace(",", ".")) / 100

    unidade_linha = preco_info.split("\n")[1]

    moeda = unidade_linha.split("/")[0].strip()
    unidade = unidade_linha.split("/")[1].strip()

    resultado = {
        "produto": produto,
        "uf": uf,
        "praca": praca,
        "data": datetime.now().isoformat(),
        "preco": preco,
        "variacao_mensal": variacao,
        "moeda": moeda,
        "unidade": unidade
    }

    return resultado