# pylint: disable=missing-docstring

# Combinando elementos.

# crear 2 listas, una de numeros y otra de nombres.
numeros = [1, 2, 3, 4, 5, 6]
nombres = ['luis', 'julio', 'raquel', 'lupe']
print(f'numeros: {numeros}')
print(f'nombres: {nombres}')

print()

# usar ZIP para combinarlos.
combinado = zip(numeros, nombres)
print(f'combinado: {combinado}')

combinado = list(combinado)
print(f'lista combinados: {combinado}')

print()
# Crear 2 listas, 1 con 5 numeros, 1 con 3 letras.
cinco_num = [1, 2, 3, 4, 5]
tres_letras = ['a', 'b', 'c']

combinado_2 = zip(cinco_num, tres_letras)  # solo combina si hace match
combinado_2 = list(combinado_2)
print(f'lista combinados 2: {combinado_2}')
