# pylint: disable=missing-docstring
import math

# Strings/CADENAS.

# slice
CADENA = 'Hola a todos'
print(CADENA[6::-1])  # el -1 invierte la CADENA.

print(CADENA[::2])  # Hl  oo imprime de a 2 caracteres.

# Metodos de Str:

# búsqueda con Find más slice para imrimir un substr.
NOMBRE = 'anabella'
print(NOMBRE[NOMBRE.find('b'):])  # bella.

# Rstrip(fin) y Lstrip(inicio): remueven caracteres(default= ' ').

MENSAJE = ' hola mundo '
print(MENSAJE.rstrip().lstrip())

# Split() transforma en lista una cadenda según un caracter.
list_MENSAJE = MENSAJE.split()
print(list_MENSAJE)

# Enumerate: tupla(posicion, caracter)
# ho = (0, 'h'), (1, 'o')
print(enumerate(NOMBRE))
print(list(enumerate(NOMBRE)))

# Mayúsculas y Minúsculas:
print(MENSAJE.upper())  # Mayus
PALABRA = 'HOLA'
print(PALABRA.lower())  # min

# Reemplazo:

print(MENSAJE.replace('hola', 'chau'))

# Format: {}=variable

# Simple:
FORMATO_1 = '{}, {}, {}'.format('uno', 'dos', 'tres')
print(FORMATO_1)

# Epecificando con posicion cual variable.
FORMATO_2 = '{2}, {0}, {1}'.format('uno', 'dos', 'tres')
print(FORMATO_2)

# Epecificando con variable.
FORMATO_3 = '{a}, {c}, {b}'.format(a='uno', b='dos', c='tres')
print(FORMATO_3)

# Imprimiendo Decimales:
print(f'{math.pi}')

# imprimir hasta tres decimales:
print(f'{math.pi:.3f}')

# ^ centrado de espacios.
print(f'|{math.e:^30} |')

# < a la izquierda(espacios).
print(f'|{math.cos(0):<30}|')
