# Biblioteca Matplotlib
# Grafico de Coluna Clusterizado
# -------------------------------------

import matplotlib.pyplot as plt

# Grafico 1: Vendas Mensais

Meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul']
Vendas = [10000, 12000,11000,11050,130000,120500,150000]

plt.bar(Meses, Vendas, color='orange')
plt.ylabel('Vendas (R$)')
plt.xlabel('Meses (1° semestre)')
plt.title('Vendas Mensais (Gráfico de coluna)')

# Exibir
plt.show()

# Grafico 2: Gasto com Alimentação
# ----------------------------------------
GastoComAlimentacao = [10000, 12000, 11000, 11050, 130000, 120500, 150000]

# Personalização do gráfico
plt.bar(Meses, GastoComAlimentacao, color='blue', alpha=0.7)
plt.ylabel('Gasto com alimentação (R$)')
plt.xlabel('Meses (1° semestre)')
plt.title('Gasto Com Alimentação 1º semestre ')
plt.ylim(1000, max(GastoComAlimentacao) + 100)
plt.grid(axis='y', linestyle=':', alpha= 0.7)

# Criar gráfico de barras
barras = plt.bar(Meses, GastoComAlimentacao, color='blue', alpha=0.7)

# Adicionar rótulos no topo de cada barra
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2, altura + 2000, f'{altura:.0f}',
             ha='center', va='bottom', fontsize=9, color='black')

plt.show()

# Grafico 3: custo de produção comparativo
# ------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

# Suponha que você tenha 6 meses
Meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
x = np.arange(len(Meses))  # Isso gera [0, 1, 2, 3, 4, 5]

# Dados de custo
Custo_2022 = [10000, 12000, 11000, 11050, 13000, 12050]
Custo_2023 = [10500, 12500, 11500, 11550, 13500, 12500]

width = 0.35  # Largura das barras

# Gráfico de barras agrupadas
plt.bar(x - width/2, Custo_2022, width, label='2022', color='blue')
plt.bar(x + width/2, Custo_2023, width, label='2023', color='green')
plt.bar(x + width, Custo_2022,width,label='2024', color='red')

plt.xticks(x, Meses)
plt.ylabel('Custo (R$)')
plt.title('Comparativo de Custos 2022 vs 2023')
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.7)

plt.show()


