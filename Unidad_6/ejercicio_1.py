# pylint: disable=missing-docstring
'''
1. Construye una lista de 10 números generados de forma pseudoaleatoria y realiza
las siguientes operaciones:
a. Multiplica todos los elementos e imprime el resultado
b. Busca e imprime el número más pequeño y más grande de la lista
c. Busca el promedio de lo números
'''
import random

lista = []
for _ in range(10):
    a = random.randint(1, 10)
    lista.append(a)

print(f'lista: {lista}')

PROD = 1
i = 0
while i < len(lista):
    PROD *= lista[i]
    i += 1
print(f'multiplicación {PROD}')

print(f'num max {max(lista)}')
print(f'num min {min(lista)}')

promedio = sum(lista) / len(lista)

print(f'promedio {promedio}')
