# Tipos primitivos de dados em python
# int     | Inteiro
# float   | Real / Ponto Flutuante
# bool    | Booleana (True, False)
# complex | Tipos Complexos
# String  | Alfanúmericos


# Variavel de Texto
texto = 'Curso de Python Trovato'   # atribuição
print(texto)
print('Tipo: ', type(texto))
print()

varNumero1 = '100'
print(varNumero1)
print(type(varNumero1))

# Variáveis para tipos numéricos

varA = 99
varB = 4.56789
varC = False
varD = 2+9j
varE = 'Python'

print(varA, varB, varC, varD, varE)
print()

print(type(varA), type(varB), type(varC), type(varD), type(varE))
print()

# Conversão de tipos

varF = float(varA)
print('Float de varF:', type(varF))
print()

varG = int(varB)
print('Int de varG:', type(varG))
print(varG)
print()

# Variáveis booleanas
varH = False
varI = True
varJ = not(False)
varK = not(True)

print(varH, varI, varJ, varK)
print()
