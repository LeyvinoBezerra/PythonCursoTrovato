import  pandas as pd

# Criar uma Series com valores de texto
# Converter para números
serie_texto = pd.Series(['1.0', '2.0', '3.0', '4.0', '5.0', '6.0'])
valores_converter = pd.to_numeric(serie_texto)
soma_valores = valores_converter.sum()

print()
print('Serie convertida para números:')
print(valores_converter)
print()
print('Somatório de valores:', soma_valores)
print()

# Exemplo 2

data = {
     'Disciplina': ['Matematica', 'Historia', 'Geografia'],
     'Nota1': ['7.0','8.5','9.0'],
     'Nota2': ['7.5','9.0','10.0'],
     'Nota3': ['7.5','9.0','10.0']
 }
df = pd.DataFrame(data)


# Conveter as colunas de notas para números
colunas_notas = ['Nota1', 'Nota2', 'Nota3']
df[colunas_notas] = df[colunas_notas].apply(pd.to_numeric)

# Calculo da média das notas de cada linha
df['Média'] = df[colunas_notas].mean(axis=1)

print()
print('DataFrame com notas convertidas e médias calculada')
print(df)
print()
