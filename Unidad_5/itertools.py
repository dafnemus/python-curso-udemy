# pylint: disable=missing-docstring

import itertools as tipo

# crear una lista iterator object
lista_iter = iter([1, 2, 3, 4, 5, 6])
list(lista_iter)
print(f'list_iterator_object: {lista_iter}')

# Crear 2 listas, 1 con 5 numeros, 1 con 3 letras. con itertools
cinco_num = [1, 2, 3, 4, 5]
tres_letras = ['a', 'b', 'c']

combinado_2 = tipo.zip_longest(cinco_num, tres_letras)
combinado_2 = list(combinado_2)
print(f'lista combinados 2: {combinado_2}')

print()

# lista con range y permutaciones Ejemplo.
ejemplo = list(range(2))
print(f'lista ejemplo: {ejemplo}')
print('permutations de lista ejemplo', end=" ")
print(list(tipo.permutations(ejemplo)))

# product de lista nombres y lista letras.

list_product = list(tipo.product(cinco_num, tres_letras))
print('product de numeros y letras')
print(list_product)
