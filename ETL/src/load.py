import pandas as pd
from config.conection import get_conn

def load_data(df_cotacoes, table_name, type_insert):
    conexao = get_conn()
    print(f"Carregando dados no banco de dados... {len(df_cotacoes)} linhas")   
    df_cotacoes.to_sql(table_name, con=conexao, if_exists=type_insert, index=False)
    conexao.close()