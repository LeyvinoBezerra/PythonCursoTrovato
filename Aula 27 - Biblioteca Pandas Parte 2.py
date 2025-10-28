import pandas as pd

# Leitura e conversão de um arquivo CSV
df = pd.read_csv('DADOS_FAKES.csv', delimiter=',')
print(df)
print()

#Primeiros registros
print(df.head())
print()

# Primeiros registros
print(df.tail())
print()

# informações sobre as colunas
print(df.info())
print()

# Tipos de Dados
print(df.dtypes)
print()

# Troca do indice para CPF
NovoIndice = df['CPF']
df.index = NovoIndice
print(df)
print()

# Salvar o Dataframe em um a pasta de trabalho
"""
df.to_excel('Dados_FAKES.xlsx', index=False)
print('Arquivo gerado com sucesso!')
print()
"""

"""lvar o Dataframe como Parquet
df.to_parquet('DADOS_FAKES.pqt', index=False)
print('Arquivo gerado com sucesso!')
print()
"""

# Ler dados de uma series no DataFrame
print(df['NOME'])
print()

# Ler várias colunas
print(df[['NOME','CIDADE', 'IDADE' ]])
print()

print('Total de registros:', df["NOME"].count())
print()

# Selecionar linhas de um DataFrame
Acima80Anos = df[df['IDADE'] > 80]
print(Acima80Anos)
print('Shabe:', Acima80Anos.shape)
print()

# Selecionar Linhas duas cidades
CidadesBabosaPontoM1 = df [df['CIDADE'].isin(['ponto', 'Barbosa'])]
print(CidadesBabosaPontoM1)
print('Shape:', CidadesBabosaPontoM1)
print()

# Selecionar linhas de duas cidades
CidadesBabosaPontoM1 = df[(df['CIDADE'] == 'ponto') | (df['CIDADE'] == 'Barbosa')]
print(CidadesBabosaPontoM1)
print('Shape:', CidadesBabosaPontoM1)
print()

# Aplicando filtro nas linhas e colunas
PessoasMais90Anos = df.loc[df['IDADE'] > 80, 'NOME']
print(PessoasMais90Anos)
print('Shape:', PessoasMais90Anos.shape)

