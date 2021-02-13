# pylint: disable=missing-docstring
import numpy as np

# crear un array 1D usando numpy.
lista_numeros_1_d = np.array([1, 2, 3, 4, 5])
print(f'lista usando Numpy {lista_numeros_1_d}')

print()
# array 2D con numpy.
lista_numeros_2_d = np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9)])
print(f'lista usando Numpy {lista_numeros_2_d}')

print()
# Crear un array del 1 al 10 con range().
rango_1_al_10 = range(10)
print(f'1 al 10: {rango_1_al_10}')
print(type(rango_1_al_10))
rango = list(rango_1_al_10)
print(f'rango con lista = {rango}')
rango_array = np.array(rango)
print(f'rango con numpy = {rango_array}')

# aplicar suma a los rangos.
# suma_1 = rango + 10  # genera un error.
suma_2 = rango_array + 10  # suma 10 a cada numero de la lista

print(f'suma en numpy {suma_2}')
