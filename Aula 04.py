# python
# Aula 04 - Python

#comentarios

a = 1 # Variavel de exemplo para comentário

# dockstring

"""
   Este é um comentario
   que ocupa várias linhas
"""

'''
Que também pode ser
com aspas simples
'''

print()
print("Se você pretende mesclar 'Simbolos' Diferente, então faça isso")
print('Ou isso "para alternar" entre aspas simples e duplas ')
print()

# print
print('Teste de saída')
print('Teste de saída \n varias linhas')
print('Curso', 'de', 'python')
print('Curso', 'de', 'python', sep='| ') # separa as partes utilizando um caracter
print('Curso', 'de', 'python', end='.') # finaliza a string com um deteminado caracter
print()
print('Curso \t de \t python') # separação por tabulador

arquivo = open('Aula  04 - saida.txt', 'a+')

print('curso', 'de', 'python', file=arquivo)
arquivo.close()

print()

# CTRL + s --> Salva o seu script

# F5 - Executar o script