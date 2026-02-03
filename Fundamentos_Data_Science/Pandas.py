# PANDAS
# Banco de Dados = DataFrame
# Importar o pandas para o código
# ETL - 
# https://pandas.pydata.org/
# https://pandas.pydata.org/docs/

"""
import pandas as pd
#INSERÇÃO E EXIBIÇÃO DE OBJETOS
# Ler o arquivo CSV usando pandas
df = pd.read_csv(r"Pandas.csv", sep=';', encoding="utf-8")
print("*"*100)
"""
#Para remover linhas superiores ao cabeçalho
# Lendo o arquivo pulando as 3 primeiras linhas
#df = pd.read_csv('caminho/do/arquivo.csv', skiprows=3)

#Mostra o cabeçalho até 5 registros
print(df.head())#pode inserir um valor