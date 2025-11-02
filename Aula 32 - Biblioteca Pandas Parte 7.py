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
dados_csv['Mês'] = dados_csv['DATA E HORA COMPRA'].str[3:5]
dados_csv['Mês'] = pd.to_numeric(dados_csv['Mês'])

print(dados_csv)

# Adcionar coluna de referência
dados_csv['Referência'] = dados_csv['DATA E HORA COMPRA'].str[6:10] + \
        dados_csv['DATA E HORA COMPRA'].str[3:5]
# Adcionar uma coluna de vendas pelo ponto
# 1) Substituir a virgula pelo ponto

dados_csv['PREÇO UNITÁRIO'] = dados_csv['PREÇO UNITÁRIO'].str.replace(',', '.')
# 1) Conveter a coluna Preço Unitario para valor Númerico
dados_csv['PREÇO UNITÁRIO'] = pd.to_numeric(dados_csv['PREÇO UNITÁRIO'])


# 3) Multiplicação entre Quantidade X preço Unitário
dados_csv['Total'] = dados_csv['QUANTIDADE'] * dados_csv['PREÇO UNITÁRIO']
# 4) Exibição dos resultados
print(dados_csv)

# Função para formatar em Reais
def formatar_em_reais(valor):
    return 'R$ {:,.2f}'.format(valor).replace(',', '.').replace('.', ',').replace('#',".")

resultadoMes = dados_csv.groupby('Mês')['Total'].sum()
print(resultadoMes.apply(formatar_em_reais))
print()

resultadoRef = dados_csv.groupby('Referência')['Total'].sum()
print(resultadoRef.apply(formatar_em_reais))

# Testara propriedade do objeto dados_csv
print(' ---------------------------------------------------------')
print('Quantidade de Registros: ', dados_csv['PRODUTO'].count())
print(' ---------------------------------------------------------')

print()

# Converter para um objeto do tipo Dataframe

df = pd.DataFrame(dados_csv)
print(df)

# Impressão do total de todas as colunas

print(df.sum())
print()

# Totalizar uma única coluna

df_total = df['Total'].sum()

print('------------------------------------------')
print('Total Geral:', df_total)
print('Total Geral Formatado:', formatar_em_reais(df_total))
print('------------------------------------------')
print()

# Exibir 4 colunas do DataFrame

print(df[['PRODUTO', 'QUANTIDADE', 'PREÇO UNITÁRIO','Total']])
print()

# Totalizando que vai percorrer linhas a linhas do datagrama

valor_total = 0

for registro in dados_csv['Total']:
    valor_total += registro

print('O valor total é:', formatar_em_reais(valor_total))
print()

# Somatório dos valores acima de R$ 5.000

valor_total = 0
diferenca = 0
limite = 9000

for registro in dados_csv['Total']:
    if registro > limite:
        valor_total += registro
    else:
        diferenca += registro

print()
print('Valor total acima de ', formatar_em_reais(limite), valor_total)
print()
print('Valor da diferença:', formatar_em_reais(diferenca))
print()