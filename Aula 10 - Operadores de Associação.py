# Operadores de Associação

print()

x = range(1, 6)

print('******* Operador in ********')
print('1 em x.......:', 1 in x)
print('99 em x......:', 99 in x)
print('1 e 3 em x...:', 1 and 3 in x)
print()

print('******* Operador not in ********')
print('1 not in x...:', 1 not in x)
print('99 not in x..:', 99 not in x)
print('1 and 3 not in x:', 1 and 3 not in x)

print()

# Operadores Lógicos

num1 = 3
num2 = 6
num3 = 9

print('num1=', num1, 'num2=', num2, 'num3=', num3)

print('num1 é maior do que o num2 E num2 é maior que num3?', num1 > num2 and num2 > num3)
print('num3 é maior do que o num2 E num2 é maior que num1?', num3 > num2 and num2 > num1)
print()

# not

print(not(False))
print(not(True))
print(not(1 == 2))
