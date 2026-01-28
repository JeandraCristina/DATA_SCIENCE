# -*- coding: utf-8 -*-

# 📌 Projeto: Análise de Vendas de Supermercado
# 📁 Dataset: Supermarket Sales
# 👩‍💻 Por: Jeandra Ribeiro


# ====================================================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ====================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Estilo dos gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# ====================================================
# 2. CARREGAMENTO DOS DADOS
# ====================================================
# Altere o caminho do arquivo se necessário
df = pd.read_csv('PROJETOS/projeto-analise-vendas/supermarket_sales.csv')

print(df.head())
print("Jeandra")


df['Total'] = (
    df['Total']
    .astype(str)
    .str.replace('R$', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)

# Visualização inicial
df.head()

# ====================================================
# 3. LIMPEZA DOS DADOS
# ====================================================
# Verificar tipos de dados
df.info()

# Verificar valores nulos
df.isnull().sum()

# Converter coluna de data, se necessário
df['Date'] = pd.to_datetime(df['Date'])

# Criar colunas auxiliares (ex: mês, ano)
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# ====================================================
# 4. ANÁLISE EXPLORATÓRIA
# ====================================================

# Total de vendas por cidade
vendas_por_cidade = df.groupby('City')['Total'].sum().sort_values(ascending=False)
print(vendas_por_cidade)

vendas_mensais = df.groupby('Month')['Total'].sum()
print(vendas_mensais)


# Ticket médio por tipo de cliente
ticket_medio = df.groupby('Customer type')['Total'].mean()
print(ticket_medio)

# Produtos mais vendidos
produtos_mais_vendidos = df['Product line'].value_counts()
print(produtos_mais_vendidos)

# Vendas por mês
vendas_mensais = df.groupby('Month')['Total'].sum()
print(vendas_mensais)

# ====================================================
# 5. VISUALIZAÇÃO DE DADOS
# ====================================================

# Gráfico: Total de vendas por cidade - Gráfico de Barras (Barplot)
sns.barplot(x=vendas_por_cidade.index, y=vendas_por_cidade.values)
plt.title('Total de Vendas por Cidade')
plt.ylabel('Total em R$')
plt.xlabel('Cidade')
plt.show()

# Gráfico: Produtos mais vendidos - Gráfico de Barras (Barplot)
sns.barplot(x=produtos_mais_vendidos.values, y=produtos_mais_vendidos.index)
plt.title('Produtos Mais Vendidos')
plt.xlabel('Quantidade')
plt.ylabel('Produto')
plt.show()

# Gráfico: Vendas por mês - Gráfico de Linha (Lineplot)
sns.lineplot(x=vendas_mensais.index, y=vendas_mensais.values, marker='o')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total em R$')
plt.show()

print("Jeandra")

# ====================================================
# 6. CONCLUSÕES
# ====================================================
print("Conclusões:")
print("- A cidade com maior faturamento é: ", vendas_por_cidade.idxmax())
print("- O tipo de cliente com maior ticket médio é: ", ticket_medio.idxmax())
print("- O produto mais vendido foi: ", produtos_mais_vendidos.idxmax())




