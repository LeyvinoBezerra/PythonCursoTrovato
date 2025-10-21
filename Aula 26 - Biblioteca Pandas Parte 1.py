# Biblioteca Pandas - Parte 1
# Series

# Sites oficial : https://pandas.pydata.org/

import pandas as pd

# Criação de um DataFrame a Partir de um Dictionary

ListasPessoas = {"Nome":["Alessandro", "Marcia", "Amanda", "Andre"],
                 "Idade": [51,50,40,50],
                 "Sexo": ["F", "M", "F", "M"]}

df = pd.DataFrame(ListasPessoas) # Tabela bidimensional (linhas e colunas)
print(df)
print()

# Series
print(df["Nome"])
print()

#criação de uma series
valores =[1,2,3,4]
valoresSeries = pd.Series(valores, index =['a','b','c','d'])
print(valoresSeries)
print()

# Acessar o primeiro elemento de uma series
print('Primeiro elemento: ', valoresSeries[0])
print('indices C....: ', valoresSeries['c'])
print()

# Nova series para ser adicionada ao DataFrame

DiaAniversario = pd.Series([11, 7, 7, 12])
print('Dia aniversario: ', DiaAniversario)
print()

# Adcionar ao Dataframe
df['Dia aniversario'] = DiaAniversario
print(df)
print()

# Métodos de uma Serie / DataFrame
print('Maior idade:', df['Idade'].max())
print('Menor idade:', df['Idade'].min())
print('Quantos nomes', df['Nome'].count())
print('Média de idades:', df['Idade'].mean())
print('Somatória de idades:', df['Idade'].sum(), 'anos')
print('classificação:', df['Idade'].sort_values())
print()

# Estatisca completo

print(df.describe())
print()

# Proxima aula: Leitura de dados em um DataFrame