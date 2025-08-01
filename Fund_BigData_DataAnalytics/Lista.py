#Lista
"""
Uma lista é uma estrutura de dados em Python que permite armazenar uma coleção de itens. 
Comandos:
"""
# Criando uma lista com alguns itens
#lista = [1, 2, 3, 4, 5]
#print(lista)

#Podemos observar a classe de uma lista com type():
#print(type(lista))

# Imprimindo o tamanho da lista
#print(len(lista)) # Output: 5

# Acessando um item específico na lista
#print(lista[2]) # Output: 3

# Adicionando um item ao final da lista
#lista.append(6)
#print(lista)

# Inserindo um item em uma posição específica da lista
#lista.insert(2, 7)
#print(lista)

# Removendo um item da lista
#lista.remove(3)
#print(lista)

# Ordenando a lista
#lista.sort()
#print(lista)

# Invertendo a ordem da lista
#lista.reverse()
#print(lista)

# Verificando se um item está na lista
#print(4 in lista) # Output: True

# Concatenando duas listas
#outra_lista = [7, 8, 9]
#lista += outra_lista
#print(lista)

# Fatiando uma lista
# lista[ inicio : fim : passo ]
#print(lista)
#parte_da_lista = lista[1:6:1]#último item ele não pega
#print(parte_da_lista)

# Repetindo uma lista
#lista *= 2
#print(lista)

# Verificando o índice de um item na lista
#print(lista.index(6))

# Contando a quantidade de vezes que um item aparece na lista
#print(lista.count(7))

#Calculos em Listas

#a = [10,20,30,50,60,40]
#b = [10,10,10,10,10,10]
#soma = 0
#media = 0
#count = 1

#for n1 in a:
#    soma = n1 + soma
#    count = count + 1 
#media = soma / count
#print("A soma é: ",soma)
#print("A média é: ",media)

#print("Calculando o Valor dos índices")
#somaI = 0
#i = 0
#while i <= 5:
#    somaI = a[i] + b[i]
#    print("A soma é: ",somaI)
#    i = i + 1
#Fim de Programa

#Funções estatísticas para listas
#a = [10,20,30,50,60,40]
#print(a)

"""SUM -> retorna a soma dos itens"""
#soma = sum(a)
#print(soma)