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