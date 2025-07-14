#Set
""" 
é uma coleção não ordenada e mutável de elementos únicos. 
Os elementos de um set são definidos entre chaves, separados por vírgula.
Operações básicas com sets:

União: set1 | set2 ou set1.union(set2)
Interseção: set1 & set2 ou set1.intersection(set2)
Diferença: set1 - set2 ou set1.difference(set2)
Diferença simétrica: set1 ^ set2 ou set1.symmetric_difference(set2)

Verificação de pertencimento:
elemento in set: Verifica se o elemento pertence ao set.

Limpar o set:
set.clear(): Remove todos os elementos do set.

Copiar o set:
set.copy(): Cria uma cópia do set.

Iteração sobre um set:
Usar for para iterar sobre os elementos do set.

Combinar sets:
set.update(set2): Adiciona os elementos de set2 a set.

Remover elemento com segurança:
set.discard(elemento): Remove o elemento do set, se existir. Se não existir, não ocorre erro.

Converter outras coleções para set:
set(iterable): Cria um novo set a partir de um iterable (lista, tupla, string, etc.).

"""
# Criando um set com algumas cores
#cores = {'vermelho', 'verde','azul', 'amarelo','vermelho','verde','verde','amarelo','vermelha'}
#print(cores)

# Adicionando uma cor ao set
#cores.add('roxo')
#print(cores)

# Removendo uma cor do set
#cores.remove('verde')
#print(cores)

# Operações básicas com sets
#set1 = {1, 2, 3, 4, 5}
#set2 = {4, 5, 6, 7, 8}

#uniao = set1.union(set2)
#intersecao = set1.intersection(set2)
#diferenca = set1.difference(set2)
#diferenca_simetrica = set1.symmetric_difference(set2)

#print("União:", uniao)
#print("Interseção:", intersecao)
#print("Diferença:", diferenca)
#print("Diferença Simétrica:", diferenca_simetrica)

# Verificação de pertencimento
#print(3 in set1)  # True
#print(9 in set1)  # False

# Copiar o set
#set_copia = set1.copy()

# Combinar sets
#set1.update(set2)
#print("Set1 após combinar com Set2:", set1)

# Remover elemento com segurança
#set1.discard(4)
#print("Set1 após remover 4:", set1)

# Converter uma lista para set
#lista = [1, 2, 3, 3, 4, 5, 5]
#set_da_lista = set(lista)
#print("Set a partir da lista:", set_da_lista)