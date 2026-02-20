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

"""
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
#NaN = Not a Number

#Remover colunas em NaN
print(df)
"""

#dropna(): É um método do pandas que é utilizado para remover linhas ou colunas com
#valores nulos (NaN). Neste caso, queremos remover colunas, então utilizamos axis=1
#para indicar que a operação será realizada ao longo das colunas.
#axis=1: É o parâmetro que informa ao método dropna() que queremos remover colunas.
#O valor 1 indica que a operação será feita ao longo das colunas, enquanto o valor 0 seria
#utilizado para remover linhas.
#how='all': É outro parâmetro do método dropna() que controla como a remoção será feita.
#Neste caso, estamos usando 'all', o que significa que a coluna será removida somente se
#todos os seus valores forem nulos (vazios).

df = df.dropna(axis=1, how='all')
print(df)

#Remover as linhas em Nan
print(df)
df = df.dropna(how="all")
print(df)

#Remover uma coluna e criar um novo DataFrame
#O DataFrame original mantêm a formação
remove_numeros = df.drop(columns=["Números"])
print(remove_numeros)
print(df)

# Supondo que você já tenha o DataFrame df carregado e a primeira linha contendo os nomes das colunas
# Define a primeira linha como cabeçalho e recria o DataFrame com o novo cabeçalho
#df.columns = df.iloc[0]
#df = df.iloc[1:].reset_index(drop=True)
#print(df)

print(df.describe())
print(df.info())

#Alterando o tipo de dados da coluna
#df['Nome_da_Coluna'] = df['Nome_da_Coluna'].astype(int)
#df['Nome_da_Coluna'] = df['Nome_da_Coluna'].astype(float)
#df['Nome_da_Coluna'] = df['Nome_da_Coluna'].astype(str)

df["Datas"] = pd.to_datetime(df["Datas"],format='%d/%m/%Y')
df["Hora"] = pd.to_datetime(df["Hora"],format='%H:%M:%S')
df["Letras"] = df["Letras"].astype(str)
df["Números"] = df["Números"].astype("float32")
print(df.info())

#Renomeando uma Coluna
df_NovoNomeColuna = df.rename(columns={"Números":"Numeros"})
print(df_NovoNomeColuna)

#Renomeando várias colunas
TodasColunas = {
    "Números":"numeros",
    "Letras":"letras",
    "Datas":"datas",
    "Valor":"valores",
    "Hora":"horas"
}
df_NovoNomeColunas = df.rename(columns=TodasColunas)
#df.rename(columns=TodasColunas, inplace=True)
print(df_NovoNomeColunas)
print(df)

#SALVANDO O BANCO DE DADOS LIMPO
df_NovoNomeColunas.to_excel('DadosLimpos.xlsx')

#Remover Caracteres existentes em dados dos registros
# Remover o caractere "@" no início dos registros da coluna "Nome_da_Coluna"
#   df['Nome_da_Coluna'] = df['Nome_da_Coluna'].str.replace('^@', '')
# Remover o caractere "#" no final dos registros da coluna "Nome_da_Coluna"
#   df['Nome_da_Coluna'] = df['Nome_da_Coluna'].str.replace('#$', '')

#Classificar Banco de Dados
Classificar_Letras = df.sort_values(by="Letras", ascending=True)
print(Classificar_Letras)
Classificar_Numeros = df.sort_values(by="Números", ascending=True)
print(Classificar_Numeros)
Classificar_Varios = df.sort_values(by=["Letras","Números"], ascending=[True, False])
print(Classificar_Varios)

#FILTRAR DADOS
"""
#Indexação booleana:
#A indexação booleana é uma forma simples e poderosa
#de filtrar os dados com base em condições específicas.
#Você cria uma condição booleana usando operadores de comparação
#(como ==, >, <, >=, <=, !=, etc.) e, em seguida, aplica essa condição ao DataFrame.
#df_filtrado = df[df['idade'] > 30]
#Método query():
#O método query() permite filtrar os dados usando uma string de consulta
#(similar a uma expressão SQL). A vantagem é que você pode escrever a condição
#de filtragem como uma string, o que pode ser útil para filtragens mais complexas.
#df_filtrado = df.query('idade > 30')

"""  

Filtrar_Letra = df.query('Letras == "b"')
print(Filtrar_Letra)

Filtra_Número = df.query('Números >= 15')
print(Filtra_Número)

Filtrar_Multiplos_and = df.query('Letras == "b" and Números >= 15')
print(Filtrar_Multiplos_and)

Filtrar_Multiplos_or = df.query('Letras == "b" or Números < 9')
print(Filtrar_Multiplos_or)

# Filtrar apenas as linhas com a data específica '2023-07-19'
data_especifica = '2023-07-19'
df_filtrado_data_especifica = df[df['Datas'] == data_especifica]
print(df_filtrado_data_especifica)

# Filtrar apenas as linhas com datas dentro do intervalo de '2023-07-20' a '2023-07-22'
data_inicio = '2023-07-20'
data_fim = '2023-07-22'
df_filtrado_intervalo_datas = df[(df['Datas'] >= data_inicio) & (df['Datas'] <= data_fim)]
print(df_filtrado_intervalo_datas)

#FUNÇÕES DO PANDAS
#FUNÇÕES BÁSICAS

Soma = df["Valor"].sum()
print("A soma é: ",Soma)

Média = df["Valor"].mean()
print("A média é: ",Média)

Mediana = df["Valor"].median()
print("A mediana é: ",Mediana)

Máximo = df["Valor"].max()
print("O maior valor é: ",Máximo)

Mínimo = df["Valor"].min()
print("A mediana é: ",Mínimo)

Contagem = df["Valor"].count()
print("O total de números é: ",Contagem)

#Funções de Data/Hora
# Extrair os componentes de data (ano, mês, dia)
df['Ano'] = df['Datas'].dt.year
df['Mes'] = df['Datas'].dt.month
df['Dia'] = df['Datas'].dt.day

# Extrair os componentes de hora (hora, minuto, segundo)
df['Hora'] = pd.to_datetime(df['Hora'])  # Se 'Hora' não estiver em formato datetime, converta primeiro  