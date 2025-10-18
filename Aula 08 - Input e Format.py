# input - Obter dados
print()

import math as m

varNome = input('Digite o seu nome: ')
print('Olá,', varNome + '!\n')

print('Calcular a área de uma circunferência\n')

varRaio = input('Informe o raio da circunferência: ') # Input do raio
varResultado = m.pi * float(varRaio) ** 2
print('Área:', varResultado)
print('Comprimento:', 2 * m.pi * float(varRaio))
print()

# 2º exemplo
# Converter graus Celsius para Farenheith

varTemperatura = float(input('Digite o valor em Celsius: '))
varResultado = (varTemperatura * 1.8) + 32
print('Farenheith:', varResultado)
print('-' * 50)

# Método format
varTexto = '{0}, seja bem-vindo(a)!'
print(varTexto.format(varNome))
print()

varIdade = 51
varProfissao = 'Analista de Treinamento na MLF'
varTexto = '{0}, seja bem-vindo(a)! \nIdade: {1} \nProfissão: {2}'
print(varTexto.format(varNome, varIdade, varProfissao))
print()

# Formatar o resultado
varResultado = m.pi * float(varRaio) ** 2
print('Área:', varResultado)
print('Comprimento:', 2 * m.pi * float(varRaio))
print()

Res_Final = 'Área: {0:.1f}ºC'
print(Res_Final.format(varResultado))
print()