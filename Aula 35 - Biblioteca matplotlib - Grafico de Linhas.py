# Biblioteca matplotlib
# Graficos de Linhas

import  matplotlib.pyplot as plt

# Dados
Meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul']

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
Custos_2022 = [1200, 13500, 1300, 14000, 13300, 14500, 13800]
Custos_2023 = [1600, 12500, 14900, 16000, 18000, 16300, 17000]
Custos_2024 = [1400, 16800, 15000, 14000, 16000, 14600, 15500]


# Criar
plt.plot(Meses, Custos_2022, marker='o', linestyle='-', color='blue',label='2022')
plt.plot(Meses, Custos_2022, marker='s', linestyle='--', color='green',label='2023')
plt.plot(Meses, Custos_2022, marker='^', linestyle=':', color='red',label='2024')

# Customizações

plt.xticks(Meses)
plt.ylabel('Custo de Produção (R$)')
plt.xlabel('1° Semestre')
plt.xlabel('Meses')
plt.title('Comporação de custo de produção (2022-20224)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(title='Ano')
plt.ylim(10000, max(Custos_2022) + 5000)
plt.show()