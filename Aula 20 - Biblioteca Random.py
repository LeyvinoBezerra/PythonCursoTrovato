# Biblioteca random
import random as rd
print()


# Controlar a seguencia de números aleatórios
print('1 Nr. : ', rd.random()) # gere um numero aleatorio com baseno estado atual do gerador
print()

estado_gerado = rd.getstate() # Captura o estado atual interno gerado
print('2° Nr. : ', rd.random())
print()

rd.setstate(estado_gerado)
print('3° Nr. : ', rd.random())
print()

# Com numerod inteiros

print('rangBang: ', rd.randrange(1,60)) # Gera números aleatorios de uma faixa de valores
print()

lista_valores = rd.sample(range(61), 6)  # exemplo da mega sena
print('sample:', lista_valores)
print()

lista_valores.sort()
print('sort', lista_valores)
print()

print('randint:', rd.randint(1,61))
print()

print('choice1:', rd.choice(lista_valores)) # para pegar numeros aleatorio dentroda lista
print()

print('choice2  :', rd.choice('Item A','Item B','Item C','Item D','Item E',))
print()

print('LISTA ORIGINAL:', lista_valores)
rd.shuffle(lista_valores) # Embaralhar

print('shuffle:', lista_valores)
print()

print('sample:', rd.sample(lista_valores, 3))
print()

print('MegaSena:', rd.sample(range(61), 6))
print()

#  https://docs.python.org/pt-br/3.7/library/random.html




