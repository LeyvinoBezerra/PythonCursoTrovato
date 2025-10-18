# Exemplo 1
print()

a = 1
while (a <= 15):
    print('Número: ', a)
    a += 1

print()

# Exemplo 2
valor = 1
limite = 7

while valor <= limite:
    print('Número:', valor)
    valor += 1

print()

# Exemplo 3

print('Somar números: (0 para sair)')

numero_usuario = 1
somatoria = 0

while numero_usuario != 0:
    numero_usuario = int(input('Digite um número inteiro: '))
    if numero_usuario == 0:
        break

    somatoria += numero_usuario

print('A soma total dos números digitados é:', somatoria)

print()

# Exemplo 4

total = 0
numero = int(input('Digite um número para adicionar à soma:'))

total += numero

while (total <= 100):
    if total > 100:
        print('A soma excedeu 100, e é:', total)
        break

    numero = int(input('Digite um número para adicionar à soma:'))
    total += numero

print('O total ultrapassou o limite de 100. Total apurado:', total)