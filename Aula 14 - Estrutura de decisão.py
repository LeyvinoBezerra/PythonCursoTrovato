from datetime import date
print()

# Tomada de decisão

quantidade = 299

if quantidade >= 150:
    print('Estoque normal...') # true
else:
    print('Estoque reduzido...') # false

print()

# Exemplo

numero = float(input('Digite um número qualquer! '))

if numero < 0:
    print('O número digitado é negativo!')
elif numero == 0:
    print('O número digitado foi zero!')
else:
    print('O número digitado foi positivo!')

print()

# Exemplo 3

data_nascimento = date(1972, 11, 11)
idade = int((date.today() - data_nascimento).days/365.25)

if idade < 12:
    print('Criança de até 11 anos')
elif idade < 18:
    print('Adolescente até 17 anos')
elif idade < 65:
    print('Adulto até 65 anos')
else:
    print('Maior ou igual a 65 anos')

print()

# Exemplo 4A

data = date(1972, 11, 11)
dia_da_semana = data.isoweekday()

if dia_da_semana >= 1 and dia_da_semana <= 5:
    print('Dia da semana', data.strftime("%A"))
else:
    print('Final de semana:', data.strftime("%A"))

print()

# Exemplo 4B

data = date(2024, 5, 4)
dia_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
dia_hoje = data.isoweekday()

if dia_hoje >= 1 and dia_hoje <= 5:
    print('Dia da semana:', dia_da_semana[dia_hoje - 1])
else:
    print('Final de semana:', dia_da_semana[dia_hoje - 1])