# Listas

# Criar a lista
minhaLista = []
print(type(minhaLista))
print()

minhaLista = ['Curso', 'Python', 'Trovato', 'Youtube']
print(minhaLista)

# Tamanho da lista
print('Tamanho da lista:', len(minhaLista))

# Tipos de dados em listas

minhaLista2 = ['1', False, 'Trovato', 1.89766, minhaLista]
print(minhaLista2)

# Unificar listas
minhaLista2 = ['1', False, 'Trovato', 1.89766]
uniaoListas = minhaLista + minhaLista2
print(uniaoListas)

# Duplicar os elementos de uma lista
listaDuplicada = minhaLista * 2
print(listaDuplicada)

# Verificar elementos da lista
print('Trovato' in minhaLista)
print('TROVATO' in minhaLista)

#Trabalhar com as listas
lstNumeros = [5, 10, 15, 20, 22, 25, 30, 55]

print('Mínimo:', min(lstNumeros))
print('Máximo:', max(lstNumeros))
print('Somatória:', sum(lstNumeros))

# Métodos
# append
minhaLista.append('Valor Adicionado')
print(minhaLista)

# insert
minhaLista.insert(0, 'Primeiro Valor') # Base 0
print(minhaLista)

# pop - Elimina elementos da lista
minhaLista3 = ['Curso', 'Python', 'Trovato', 'Youtube']
print(minhaLista3)

minhaLista3.pop() # o último registro
print(minhaLista3)

minhaLista3.pop(0) # o primeiro registro
print(minhaLista3)

# remove
minhaLista3.remove('Trovato')
print(minhaLista3)


# sort | reverse

minhaLista3 = ['Youtube', 'Curso', 'Trovato', 'Python', 'Aula 12']
print(minhaLista3)

minhaLista3.sort()
print(minhaLista3)

minhaLista3.reverse()
print(minhaLista3)

minhaLista3 = minhaLista3 * 3
print('Qtd.Python:', minhaLista3.count('Python'))
print('Qtd.VBA:', minhaLista3.count('VBA'))

print()

print(minhaLista3[1])