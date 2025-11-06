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

# Grafico 2: Gastocom Alimentação
# ----------------------------------------