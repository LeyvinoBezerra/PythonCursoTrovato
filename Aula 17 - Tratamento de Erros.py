# Tratamento de erros no Python
print()

try:
   print(variavel_A)
except:
   print('Erro no código!')

print()

try:
   print(variavel_B)
except NameError:
   print('A variável utilizada não foi definida! Verifique!')
except:
   print('Erro!')

print()

try:
   print('Acesse o catálogo: http://bit.ly/trovatoPBI')
except:
   print('Há um erro! Verifique!')
else:
   print('Rotina executada com sucesso!')

print()

# Abertura de um arquivo de texto

try:
   arquivo = open('MeuArquivo.txt', 'r')
   try:
      arquivo.write('Grave essa linha no arquivo...')
   except:
      print('Não foi possível salvar a mensagem!')
   finally:
      arquivo.close()
except:
    print('Há problemas para abrir o arquivo')

print()

# resultado = 100/0

print()

try:
   variavel_C = 100 / 0
   print(variavel_C)
except ZeroDivisionError:
   print('Você está fazendo uma divisão por zero!')
else:
   print('Cálculo efetuado com sucesso!')

print()