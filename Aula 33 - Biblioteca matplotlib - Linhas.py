# Biblioteca matplotlib
# Graficos de Linhas

import  matplotlib.pyplot as plt

# Dados
Meses = ['Jan','Fev','Abr','Mai','Abr','Mai','Jun']
Vendas = [10000, 12000,11000,11050,130000,120500,150000]

# Criar o Gráfico
plt.plot(Meses, Vendas)

# Exibir o Gráfico
plt.show()

# Gasto com Alimentação
# Perioldo semestral

# Dados
GastoAlimentacao = [1805.23, 1750.12, 1500.15, 2100.89, 1758.22, 1899.99,2000.0]

# o gráfico de linhas
plt.plot(Meses, GastoAlimentacao, marker='o', linestyle='--', color='blue',linewidth=2, markersize=8)

# Customização
plt.xticks(Meses)
plt.ylabel('Gasto Alimentacao')
plt.xlabel('Meses')
plt.title('Gasto Alimentação - Grafico de Linha')
plt.grid(True, linestyle=':', alpha=0.7)
plt.ylim(min(GastoAlimentacao) - 100, max(GastoAlimentacao)+ 100)
plt.show()

# Custo de produção comparando 3 anos
# -----------------------------------

# Dados
Custo_2022 = [12000, 15000, 13000, 14000, 16000, 17000]
Custo_2023 = [12500, 15500, 12500, 14900, 15975, 17999]
Custo_2022 = [13700, 16800, 15000, 14000, 16000, 14555]



