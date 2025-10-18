# Estrutura de Repetição FOR

print()

nomes = ['ALESSANDRO', 'TROVATO', 'CURSO DE PYTHON', 'YOUTUBE', 'PYTHON']

for x in nomes: # para cada nome na lista de nomes...
    print(x)

print()

for numeros in range(11):
    print(numeros * 2.5)

print()

nome_completo = 'Alessandro Trovato C. de Andrade'

for parte_nome in nome_completo:
    print(parte_nome)

print()

lista_nomes = ['ALESSANDRO', 'MARCIA', 'PYTHON']

for nomes in lista_nomes:
    print(nomes)
else:
    print('xxx FIM xxx')

print()

for x in nome_completo:
    print(x)
    if x == ' ':
        break
else:
    print('xxx FIM xxx')

print()