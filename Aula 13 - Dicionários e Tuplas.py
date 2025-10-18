# Tuplas

# Listas [ ]
# Tuplas ( ) -- Imutáveis

print()

tupla1 = 'a', 'd', 1, 2, {1,2,3}
tupla2 = ('a', 'd', 1, 2, {1,2,3})

print(tupla1, '\n', tupla2)
print (type(tupla1), '\n', type(tupla2))

# tupla1[1] = 'Atualizar'

tupla3 = 'Alessandro'
print(type(tupla3))

# tupla vazia

tupla4 = ()
print(tupla4)

# tupla4[0] = 'Alessandro'   # utilize uma lista
# print(tupla4)

# Declaração explicita de criação de uma tupla

tupla5 = tuple("abc")
print(type(tupla5))

print()
print('-' * 30)
print()

print('Dicionários')

dicionarioA = {1: 'Alessandro', 2: 'Márcia'}
print(dicionarioA)
print(type(dicionarioA))

# quantidade de elementos

print(len(dicionarioA))

# Adicionar valores

dicionarioA[3] = 'Paulo'
dicionarioA[4] = 'José Carlos'
print(dicionarioA)

# Update

dicionarioA.update({1: 'Novo instrutor'})
print(dicionarioA)

# Apagar itens

del(dicionarioA[1])
print(dicionarioA)

print('Keys (chaves)......:', dicionarioA.keys())
print('Items (itens)......:', dicionarioA.items())
print('Values (valores)...:', dicionarioA.values())

print()