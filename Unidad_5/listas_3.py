# pylint: disable=missing-docstring

# Ordenando Listas.

nombres = ['luis', 'pablo', 'lola', 'julieta']

# CON SORTED
nombres_ordenados = sorted(nombres)
print(f'nombres ordenados(sorted): {nombres_ordenados}')

# CON SORT DE LA A - Z
nombres.sort()
print(f'nombres ordenados A-Z(sort): {nombres}')

# CON SORT DE LA Z - A.
nombres.sort(reverse=True)
print(f'nombres ordenados Z-A(sort): {nombres}')

# DE LISTA A STRING.
CADENA_NOMBRES = ', '.join(nombres)
print(f'nombres: {CADENA_NOMBRES}')
