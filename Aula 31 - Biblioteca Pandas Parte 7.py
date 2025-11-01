# Análise de dados com o Python
# Leitura de um arquivo CSV para o DataFrame

import pandas as pd

# Leitura do arquivo CSV
dados_csv = pd.read_csv(
    filepath_or_buffer='VENDAS - Último Ano.csv', sep=';', encoding='utf8'
)

# print(dados_csv)

# Verificando se há dados nulos
print(dados_csv.isna().sum())
print()