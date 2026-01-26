# MATPLOTLIB

# https://matplotlib.org/
# https://matplotlib.org/stable/contents.html

"""
Biblioteca muito popular em Python para a criação de gráficos e
visualizações de dados. Ele oferece uma ampla variedade de funções
para produzir gráficos de alta qualidade em diferentes formatos,
tornando-o uma excelente ferramenta para análise de dados e comunicação visual.
Duas Interfaces:
Interface orientada a objetos: onde você cria e manipula explicitamente objetos de figura e eixos.
Interface baseada em pyplot: onde você usa funções de alto nível semelhantes às do MATLAB.
"""

from matplotlib import pyplot as plt
import numpy as np

'''
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Crie um grafico de linhas, anos no eixo x, pib no eixo y
plt.plot(years, pib, color='green', marker='o', linestyle='solid') 

#adicione um titulo
plt.title("Nominal PIB")

#adicione um rotulo ao eixo y
plt.ylabel("Bilhões de Dolares")
plt.show()
'''

'''
#GRÁFICO DE LINHAS (Simples)
# Dados para o gráfico de linha
x = [1, 2, 3, 4, 5]
y = [10, 15, 5, 12, 7]
# Criar o gráfico de linha usando a função plot
plt.plot(x, y)
# Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
# Adicionar título ao gráfico
plt.title('Gráfico de Linha Simples')
# Exibir o gráfico
plt.show()
'''

'''
#GRÁFICO DE BARRAS
# Dados para o gráfico de barras
categorias = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
valores = [20, 10, 12, 15, 5, 23, 25]
# Criar o gráfico de barras usando a função bar
plt.bar(categorias, valores)
# Criar os Rótulos do Gráfico
plt.xlabel('Categoria')
plt.ylabel('Valores')
# Adicionar título ao gráfico
plt.title('Gráfico de Barras')
# Exibir o gráfico
plt.show()
'''

'''
#GRÁFICO DE BARRAS AGRUPADAS
# Dados para o gráfico de barras agrupadas
import matplotlib.pyplot as plt
# Dados para o gráfico de barras agrupadas
categorias = ['A', 'B', 'C', 'D']
valores1 = [10, 15, 5, 12]
valores2 = [8, 12, 6, 9]
# Posições no eixo X para cada grupo de barras
pos = np.arange(len(categorias))
print(pos)
# Largura das barras
largura = 0.4
# Criar o gráfico de barras agrupadas
plt.bar(pos - largura/2, valores1, largura, label='Valores 1')
plt.bar(pos + largura/2, valores2, largura, label='Valores 2')
# Definir rótulos para os eixos X e Y
plt.xlabel('Categorias')
plt.ylabel('Valores')
# Definir rótulos para as posições no eixo X
plt.xticks(pos, categorias)
# Adicionar legenda
plt.legend()
# Adicionar título ao gráfico
plt.title('Gráfico de Barras Agrupadas')
# Exibir o gráfico
plt.show()
'''

'''
# GRÁFICO DE DISPERSÃO
x = [1, 2, 3, 4, 5]
y = [10, 15, 5, 12, 7]
# Criar o gráfico de dispersão usando a função scatter
plt.scatter(x, y)
# Adicionar rótulos aos eixos e título ao gráfico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')
# Exibir o gráfico
plt.show()
'''

'''
#GRÁFICO DE PIZZA
tamanhos = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']
# Criar o gráfico de pizza usando a função pie
plt.pie(tamanhos, labels=labels, autopct='%1.1f%%', startangle=90)
# Adicionar título ao gráfico
plt.title('Gráfico de Pizza')
# Exibir o gráfico
plt.show()
'''

# HISTOGRAMA
dados = [5, 10, 15, 20, 25, 25, 30, 30, 30, 35, 35, 40, 45]
# Criar o histograma usando a função hist
plt.hist(dados, bins=5, edgecolor='black')
# Adicionar rótulos aos eixos e título ao gráfico
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')
# Exibir o gráfico
plt.show()


import matplotlib.pyplot as plt
# Dados para os gráficos
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 5, 12, 7]
y2 = [5, 8, 3, 9, 10]
y3 = [20, 18, 25, 30, 22]
y4 = [12, 5, 10, 8, 16]
# Criar uma figura e uma grade de 2x2 subplots
fig, axs = plt.subplots(2, 2)
# Plotar os gráficos em cada subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Gráfico 1')
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Gráfico 2')
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Gráfico 3')
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Gráfico 4')
# Ajustar o layout para evitar sobreposição de títulos 
plt.tight_layout
