# Python_NumPy:
"""
O NumPy é uma das bibliotecas mais populares do Python para
computação numérica. Ele fornece uma estrutura de array multidimensional rápida e eficiente, bem como funções matemáticas para trabalhar com esses arrays. Utilizada para ciência de dados em aprendizado de máquina.
O NumPy é uma biblioteca focada em computação numérica e
manipulação eficiente de arrays multidimensionais. Embora ele
não seja voltado especificamente para funções de data, hora e texto,
existem outras bibliotecas do ecossistema Python que podem ser usadas
em conjunto com o NumPy para trabalhar com esses tipos de dados.
Em resumo, o NumPy é poderoso para computação numérica e manipulação
de arrays, mas para trabalhar com data, hora e texto, você pode combinar
o NumPy com outras bibliotecas Python, como datetime e pandas, para obter funcionalidades mais específicas.
"""

#pip install numpy
import numpy as np
#Você pode criar arrays do NumPy de várias maneiras: A partir de listas Python:
# Array unidimensional (vetor)
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
# Array bidimensional (matriz)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Funções Especiais NumPy
# Array de zeros com dimensão (3, 4)
zeros_arr = np.zeros((3, 4))
print(zeros_arr)
# Array de uns com dimensão (2, 5)
ones_arr = np.ones((2, 5))
print(ones_arr)
# Array com valores aleatórios entre 0 e 1 com dimensão (2, 3)
random_arr = np.random.rand(2, 3)
print(random_arr)

#Indexação e Fatias (Slicing):**
# Assim como as listas do Python, os arrays do NumPy também podem ser acessados e fatiados:
arr = np.array([1, 2, 3, 4, 5])
# Acessando elementos individuais
print(arr[0])  # Saída: 1
print(arr[3])  # Saída: 4
# Fatiando o array
print(arr[1:4])  # Saída: [2, 3, 4]

# OPERAÇÕES MATEMÁTICAS:
# O NumPy permite realizar operações matemáticas em arrays de maneira eficiente:
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Soma de arrays
result_sum = a + b  # Saída: [5, 7, 9]
print(result_sum)
# Subtração de arrays
result_subtract = b - a  # Saída: [3, 3, 3]
print(result_subtract)
# Multiplicação de arrays (elemento a elemento)
result_multiply = a * b  # Saída: [4, 10, 18]
print(result_multiply)
# Produto interno (produto escalar) de arrays
result_dot_product = np.dot(a, b)  # Saída: 32
print(result_dot_product)

# Funções de Data e Hora:
# Para trabalhar com data e hora, uma das bibliotecas mais populares
# é o datetime. O NumPy pode armazenar objetos datetime em arrays,
# e você pode realizar operações matemáticas com eles.

from datetime import datetimetes = np.array([datetime(2023, 7, 1), datetime(2023, 7, 15), datetime(2023, 7, 25)])
# Diferença entre duas datas
time_difference = dates[2] - dates[0]
print(time_difference)  # Saída: 24 days, 0:00:00

# Funções de Texto:**
# Para manipulação de texto, uma biblioteca comum é a str do Python.
# Enquanto o NumPy não possui funções de texto específicas, você pode
# aplicar funções de string do Python em arrays do NumPy usando a função np.vectorize.
# Função que retorna o comprimento de uma string
def str_length(text):
        return len(text)
# Vetorizando a função para aplicá-la em um array de strings
vectorized_str_length = np.vectorize(str_length)
