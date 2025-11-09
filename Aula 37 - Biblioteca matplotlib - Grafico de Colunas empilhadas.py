# Matplotlib
# Gráfico de coluna Empilhado ou 100% Empilhado


import matplotlib.pyplot as plt
import numpy as np

# Dados
x = ['Cidade A', 'cidade B', 'cidade C']
Aluminio = np.array([5,10,7])
Ferro = np.array([10,15,9])
Platico = np.array([8, 12, 10])

# Criar o gráfico
plt.bar(x, Aluminio, label='Aluminio', color='gray')
plt.bar(x, Ferro, bottom=Aluminio, label='Ferro', color='green')
plt.bar(x, Platico, bottom=Aluminio + Ferro, label='Ferro', color='blue')

# customização
plt.xlabel('Cidades')
plt.ylabel('Quantidade de lixo reciclado (ton)')
plt.title('Reciclagem de lixo - Distribuida de material')
plt.legend(title='Tipo de Materiais')
plt.show()

# Grafico 2 - 100% colunas empilhadas

# Dados
total = Aluminio + Ferro + Platico
Aluminio_Porc = Aluminio / total
Ferro_Porc = Ferro / total
Plastico_Porc = Platico / total

# Criar o grafico
plt.bar(x, Aluminio_Porc, label='Aluminio', color='silver')
plt.bar(x, Ferro_Porc, bottom=Aluminio_Porc, label='Ferro', color='gray')
plt.bar(x, Plastico_Porc, bottom=Aluminio_Porc + Ferro_Porc, color='green', label='Platico')

# customização
plt.xlabel('Cidades')
plt.ylabel('Quantidade de lixo reciclado (ton)')
plt.title('Reciclagem de lixo - Distribuida de material')
plt.legend(title='Tipo de Materiais')

# Formatação do eixo y
from matplotlib.ticker import FuncFormatter
def percent(x, pos):
    return f'{x*100:.2f}%'

plt.gca().yaxis.set_major_formatter(FuncFormatter(percent))
plt.show()
