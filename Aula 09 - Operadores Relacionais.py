# Operadores Relacionais
print()

# > maior
# < menor
# >= maior ou igual
# <= menor ou igual
# != diferente
# == igual

valorA = 20
valorB = 150
valorC = 30

print('valorA: ', valorA, 'valorB: ', valorB, 'valorC: ', valorC)
print()

print('b é maior que a?', valorB > valorA)
print('b é menor que c?', valorB < valorC)
print('c é igual a 10?', valorC == 10)
print('c é maior ou igual a b?', valorC >= valorB)
print('a é diferente de 20?', valorA != 20)
print()

# IF | SE - Função de teste lógico

if valorA > valorC:
    print('A é maior que C')
else:
    print('C é maior que A')
print()

#WHILE

valorA = 1
while valorA < 10:
    print('Ciclo while: ', valorA)
    valorA += 1
print()