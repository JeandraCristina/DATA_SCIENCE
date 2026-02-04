# PANDAS
# Banco de Dados = DataFrame
# Importar o pandas para o código
# ETL - 
# https://pandas.pydata.org/
# https://pandas.pydata.org/docs/


import pandas as pd
#INSERÇÃO E EXIBIÇÃO DE OBJETOS
# Ler o arquivo CSV usando pandas
df = pd.read_csv(r"Fundamentos_Data_Science/Pandas - Pandas.csv", sep=';', skiprows=3, encoding="utf-8")
print("*"*100)
'''
#Para remover linhas superiores ao cabeçalho
# Lendo o arquivo pulando as 3 primeiras linhas
#df = pd.read_csv('caminho/do/arquivo.csv', skiprows=3)

#Mostra o cabeçalho até 5 registros
print(df.head())#pode inserir um valor
print("*"*100)

#Mostra o final até 5 registros
print(df.tail())#pode inserir um valor
print("*"*100)

#Mostra informações das colunas e tipos
print(df.info())
print("*"*100)

#Mostra um resumo dos possíveis campos calculados
print(df.describe())
print("*"*100)
'''

#count: Indica a contagem de valores não nulos na coluna.
#mean: Representa a média dos valores na coluna.
#std: É o desvio padrão dos valores na coluna.
#min: Indica o valor mínimo na coluna.
#25%: Representa o primeiro quartil ou percentil 25% dos valores.
#50%: É a mediana dos valores na coluna. A mediana é o valor que divide os dados em duas partes iguais.
#75%: Representa o terceiro quartil ou percentil 75% dos valores.
#max: Indica o valor máximo na coluna "Números".

#Exibição de Colunas
#Pode ser exibido várias colunas.
print(df['Letras'],df['Hora'])
print("*"*100)

#Seleciona linha por rótulos de linhas e colunas
print(df.loc[5,["Letras"]])
print(df.loc[2,["Letras"]])
print(df.loc[6])
print(df)

#Seleciona linha por índice de linhas e de colunas
print(df.iloc[1,0])
print(df.iloc[2,1])
print(df.iloc[3])

#MANIPULAÇÃO DE DADOS