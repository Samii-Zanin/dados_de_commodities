from datetime import datetime
import time
from dotenv import load_dotenv
import os
from src.extract import obter_cotacoes
from src.transform import transformar_dados
from src.load import load_data


load_dotenv()
tabela = os.getenv("DB_TABLE")
HORARIO_EXECUCAO = ["18:43:01", "00:34:31"]

def dag():
    df_cotacoes = obter_cotacoes()
    load_data(df_cotacoes, tabela, "append")

# Schedule para rodar a DAG nos horários definidos em HORARIO_EXECUCAO
# while True:
#     hora_atual = datetime.now().strftime("%H:%M:%S")
#     if hora_atual in HORARIO_EXECUCAO:
#         print(f"Hora atual: {hora_atual}. Iniciando execução da DAG...")
#         time.sleep(1)  # Evita múltiplas execuções no mesmo segundo
#         dag()
#     else:
#         print(f"Hora atual: {hora_atual}. Aguardando próxima execução...")
#         time.sleep(1)

#Caso queira rodar a DAG apenas uma vez, descomente a linha abaixo e comente o loop acima

dag()