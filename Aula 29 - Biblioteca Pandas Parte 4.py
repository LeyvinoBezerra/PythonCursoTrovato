import pandas as pd

# Ler a planilha do Excel
df = pd.read_excel('notas.xlsx')


# Converter as colunas de notas para números
colunas_notas = ['Nota1', 'Nota2', 'Nota3', 'Nota4']
df[colunas_notas] = df[colunas_notas].apply(pd.to_numeric)

# Calcular a média das notas para cada linha
df['Média'] = df[colunas_notas].mean(axis=1)

# Salvar o Data Frame atualizado - Excel
df.to_excel('notas_atualizadas.xlsx', index=False)
print()

# Gravação no proprio arquivo

#Ler planilhas do excel
df2 = pd.read_excel('notas.xlsx')

# Converter as colunas de notas para números
colunas_notas2 = ['Nota1', 'Nota2', 'Nota3', 'Nota4']
df2[colunas_notas2] = df2[colunas_notas2].apply(pd.to_numeric)

# Calcular a média das notas para cada linha
df2['Média'] = df2[colunas_notas2].mean(axis=1)

# Salvar o retorno na mesma pasta de trabalho

with pd.ExcelWriter('notas.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
     df.to_excel(writer, index=False, sheet_name='Resultado')

     print("Notas convetido para arquivo notas.xlsx")
     print()


# Exemplo de criação do resultado em nova coluna (Aprovado e Reprovado)

dados_excel = pd.read_excel('notas2.xlsx')

print(dados_excel.shape)
print()

for index, row in dados_excel.iterrows():
    if row['Notas'] > 5:
        dados_excel.loc[index, 'Aprovado'] = 'Sim'
    else:
        dados_excel.loc[index, 'Aprovado'] = 'Não'
print(dados_excel)

excel = pd.ExcelWriter('notas_situacao_alunos.xlsx')
dados_excel.to_excel(excel, sheet_name='Resultado', index=False)

excel.close()

print('ok')
print()
