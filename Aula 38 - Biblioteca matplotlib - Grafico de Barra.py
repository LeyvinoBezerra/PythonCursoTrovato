# Biblioteca matplotlib
# Gráfico de barras

import matplotlib.pyplot as plt
import numpy as np

# Gráfico 1: Vendas mensas
#-------------------------------
Meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
Vendas = np.random.randint(1900, 4500, size=6)

plt.barh(Meses, Vendas, color='orange')

# customização
plt.xlabel('Vendas (R$)')
plt.ylabel('Meses (1° Semestre)')
plt.title('Vendas Mensais')

plt.show()
# Gráfico 2: Gastos com alimentação
# ---------------------------------
GastosAlimentacao = np.random.randint(1000, 2000, size=6)

plt.barh(Meses, GastosAlimentacao, color='blue', alpha=0.7)

# Customização
plt.xlabel('Gasto com Alimentação (R$)')
plt.ylabel('Meses')
plt.xlim(1000, max(GastosAlimentacao)+ 100)
plt.grid(axis='x', linestyle=':', alpha=0.7)

plt.show()

# Grafico 3: custo de produção

Custo_2022 = np.random.randint(10000, 19999, size=6)
Custo_2023 = np.random.randint(10000, 19999, size=6)
Custo_2024 = np.random.randint(10000, 19999, size=6)

x = np.arange(len(Meses))
width = 0.25

plt.barh(x - width, Custo_2022, label = '2022', color='blue')
plt.barh(x, Custo_2023, label = '2023', color='green')
plt.barh(x + width, Custo_2024, label = '2024', color='red')

# Customização
plt.yticks(x, Meses)
plt.xlabel('Custo de Produção (R$)')
plt.ylabel('Meses')
plt.title('Comparaçaõ dos custo de produção  (2022-2024)')
plt.legend(title='Anos')
plt.xlim(0, max(Custo_2024)+500)
plt.show()
plt.show()