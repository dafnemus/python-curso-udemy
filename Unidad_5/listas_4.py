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
