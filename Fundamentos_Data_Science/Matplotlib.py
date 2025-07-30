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