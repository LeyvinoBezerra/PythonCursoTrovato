import os


print(os.name) #Windows = nt # Linux = Posix

print(os.environ.get('username'))       # usuario logado
print(os.environ.get('path'))           # Lista as pasta do path
print(os.environ.get('computername'))   # Nome do Computador

# Mostrar os parametros da Environ
for param in os.environ:
    print('param:', f"{param}: os.environ.get(param)")

print()

# Manipular ou acessar o sistema de arquivo

unidade = 'c:\\'
caminhoA = 'temp'
caminhoB = 'poderApagar'

print(os.path.join(unidade, caminhoA, caminhoB))
print(os.getcwd())
print()

caminhoCompleto = os.path.join(os.getcwd(), 'Teste.py')
print('Caminho + arquivo...:',caminhoCompleto)
print('Caminho sem arquivo...:',os.path.dirname(caminhoCompleto))
print('Diretorio Atual (pasta aberta):', os.curdir)
print('Somente arquivo:', os.path.basename(caminhoCompleto))
print()

# Testar se um diretorio existe

caminho = os.path.join(os.getcwd(), 'temp')
print('Caminho existe? ', os.path.exists(caminho))
print()

if os.path.exists(caminho):
    print('A Pasta Existe...')
    os.rmdir('temp')
    print('A pasta foi apagada... 8-)')
else:
    print('A pasta não existe...')
    os.mkdir('temp')
    print('A pasta foi criada...8-)')

print()
# Verificacao o tipo objeto
print(os.path.isdir(caminho)) # checa se é um diretorio
print(os.path.isdir(caminhoCompleto))
print(os.path.isfile(caminhoCompleto))
print()

#Mudar de diretorio

if os.path.exists(caminho):
    os.chdir('temp')
    print('Caminho Atual..., os.getcwd()=', os.getcwd())
    print()
else:
    print('caminho não encontrado')
    os.chdir('../')
    print(os.getcwd())