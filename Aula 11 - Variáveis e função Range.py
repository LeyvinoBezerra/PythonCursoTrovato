# Variáveis
print()

varA = 10
varB = 'Alessandro'
varC = False
varD = 1.34567
varE = varA + varD

print(type(varA), type(varB), type(varC), type(varD), '\nResultado:', varE)
print()

# Escopo de variáveis

def Funcao1(a):
    print(5 + varF)

def Funcao2(a):
    varG = 100
    print(a * varF + 100)

varF = int(input('Digite um número inteiro: '))

Funcao1(25)
Funcao2(100)

#print(varG + varF)

print()

# Função RANGE
# primeiro (inclusivo)
# último (exclusivo)

varH = range(4)  # 0, 1, 2, 3 -- Base 0
print(type(varH))

print(list(varH))

print(list(range(2, 10))) # -1
print(list(range(2, 10, 2)))
print(list(range(0, -10, -1)))

print()