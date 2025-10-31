# Método iloc
# Utiliza indice inteiros para acessar os dados
# Acessa linhase colunas pela posição (indice numérico).
# inclui o ponto inicial, mas exclui o ponto final ao selecionar intevalos

import pandas as pd

df = pd.read_excel('notas2.xlsx')
print(df)
print()

# Retorna a primeira linha de um DataFrame
print(df.iloc[0])
print()

# retorna a útima linha de um DataFrame
print(df.iloc[-1])
print()

print(df.iloc[3:15])
print()

# Selecionar os 10 últimos registros
print(df.iloc[:3])
print()

# Selecionar a segunda coluna da primeira linha
print('Nota: ', df.iloc[0,1])
print()

# Selecionar as 10 primeiras linhas e segunda coluna
print(df.iloc[0,2])
print()

# Selecionar todas as linhas de uma coluna
print(df.iloc[:2,:1])
print()

# Selecionar todas as colunas de uma linha
print(df.iloc[:, 0])
print()

# Modificar a nota do aluno 1
df.iloc[0, 1] = 10
print(df.loc[df['Nome'] == 'Aluno 1'])
print()

# Selecionar um intevalo de linhas e todas as colunas
intervalo = df.iloc[1:3, :]
print(intervalo)
print()
