# Método loc e iloc

import pandas as pd

df = pd.read_excel('notas.xlsx')
print(df)
print()

# Método loc: Utiliza rótulos (labels) para acessar os dados.
#             Pode ser usado para acessar linhas e colunas por seus nomes.
#             Inclui tanto o ponto inicial quanto o ponto final ao selecionar intervalos.

# Retornar a primeira linha de um DataFrame
print(df.loc[0]) # base 0
print()

# Retorna as 3 primeiros linhas de um DataFrame
print(df.iloc[0:2])
print()

# Retorna a quinta linha de um DataFrame
print(df.iloc[4])
print()

# Acessar o Aluno 123
print(df.loc[df['Nome'] == 'Aluno 123'])
print()

dados_aluno1 = df.loc[df['Nome'] == 'Aluno 1']
print(dados_aluno1)
print()

# Todos os Alunos com nota igual a 5

dados_notasMenor5 = df.loc[df['Nota'] == 5]
print(dados_notasMenor5)
print()

dados_notasEntre5e7 = df.loc[(df['Nota'] >= 7) & (df['Nota'] <= 7)]
print(dados_notasEntre5e7)
print()

dados_Alunos1e109 = df.loc[(df['Nome'] == 'Aluno 1') | (df['Nome'] == 'Aluno 109')]
dados_NomeContem10 = df.loc[df['Nome'].str.contains('10', regex=False)]
print(dados_NomeContem10)
print()