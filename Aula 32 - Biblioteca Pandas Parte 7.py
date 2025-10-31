# Análise de dados com o Python
# Leitura de um arquivo CSV para o DataFrame

import pandas as pd

# Leitura do arquivo CSV
dados_csv = pd.read_csv(
    filepath_or_buffer='VENDAS - Último Ano.csv', sep=';', encoding='utf8'
)

# print(dados_csv)

# Verificando se há dados nulos
#print(dados_csv.isna().sum())

#Aplicar um filtro para valores nulos
#print(dados_csv[dados_csv.isna().any(axis=1)])

#adcionar uma coluna de Mes
dados_csv['Mês'] = dados_csv['DATAS E HORA COMPRA'].str[3:5]
dados_csv['Mês'] = pd.to_numeric(dados_csv['Mês'])

# Adcionar coluna de referência
dados_csv['Referência'] = dados_csv['DATA E HORA COMPRA'].str[6:10] + \
        dados_csv['DATAS E HORA COMPRA'].str[3:5]
# Adcionar uma coluna de vendas pelo ponto
# 1) Substituir a virgula pelo ponto

dados_csv['PREÇO UNITÁRIO'] = dados_csv['PREÇO UNITÁRIO'].str.replace(',', '.')
# 1) Conveter a coluna Preço Unitario para valor Númerico
dados_csv['PREÇO UNITÁRIO'] = pd.to_numeric(dados_csv['PREÇO UNITÁRIO'])


#3) Multiplicação entre Quantidade X preço Unitário
dados_csv['Total'] = dados_csv['Quantidade'] * dados_csv['PREÇO UNITARIO']
# 4) Exibição dos resultados
print(dados_csv)

# Função para formatar em Reais
def formatar_em_reais(valor):
    return 'R$ {:,.2f}'.format(valor).replace(',', '.').replace('.', ',').replace('#','.')