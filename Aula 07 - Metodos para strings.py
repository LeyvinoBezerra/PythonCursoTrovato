# Método é um procedimento que pode manipular atributos de objetos para qual
# o método foi chamado.

print(type('texto'))
print('texto de exemplo'.capitalize())

# Concatenação de textos (strings)
textoA = 'Curso'
textoB = 'Python'
textoC = 'Trovato'
Resultado = textoA + ' ' + textoB + ' ' + textoC
print(Resultado.upper())
print()

varA, varB = 99, 199
print('Resultado ' + str(varA + varB))
print()

# Métodos para os textos

varTexto = 'Curso Python Trovato'

#Preenchimento com caracteres

print(varTexto.ljust(50, '.'))
print(varTexto.ljust(50) + '|')

print(varTexto.rjust(50, '-'))
print(varTexto.rjust(50))

print(varTexto.center(50, '.'))
print(varTexto.center(50))
print()

exit()

# Repetição de caracteres
print('x' * 50)
print()

# Alteração da caixa das palavras A/a
varTexto = 'curso Python trovato'
print('Resultado do método title()', varTexto.title())
print('alessandro trovato'.title())
print()

print(varTexto.upper())
print(varTexto.lower())
print()

print('Alessandro'.swapcase())
print()

# Função len (tamanho de uma string)

print(len(varTexto))
print(len('Alessandro Trovato'))
print()

# Extração de texto
print(varTexto[0:5])
print(len(varTexto[0:5]))
print(varTexto[6])
print(varTexto[6:])
print(varTexto[:5])

# Eliminar espaços desnecessários
varTexto = '          Curso de Python       '
print('Tamanho antes da limpeza', len(varTexto))
print(varTexto.strip())
print('Tamanho depois da limpeza', len(varTexto.strip()))
print()

# Concatenar caracteres a sua string

varTexto = 'Python'
print('-'.join(varTexto))
print()
