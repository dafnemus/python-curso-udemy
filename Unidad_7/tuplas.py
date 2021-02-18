# pylint: disable=missing-docstring
import time

# Tuplas:

# acceder a un VALOR.
mi_tupla = (1, 2, 3)
print(mi_tupla)

VALOR_1 = mi_tupla[0]
print(VALOR_1)

# Tupla vs listas.
# Las tuplas son más veloces.
# Definir una tupla y tomar el tiempo. Hacer lo mismo con lista.
# uso de TIMEIT.TIMEIT(...)

VALOR = 10000000

# con TUPLA:
START = time.time()
for x in range(VALOR):
    x = (1, 2, 3, 4, 5)
end = time.time()
print(f'tiempo en segundos con TUPLA: {end - START}s')

# con LISTA:
start = time.time()
for x in range(VALOR):
    x = [1, 2, 3, 4, 5]
end = time.time()
print(f'tiempo en segundos con LISTA: {end - start}s')

# Chequeo de si hay elementos repetidos.

elementos = ('la', 'la', 'la')

# chequeo = list_bool
chequeo = [elemento == elementos[0] for elemento in elementos]

print(chequeo)

# funcion all(si todos son verdad):
print(all(elementos))

# Chequeo de si hay 1 VALOR distinto.

mis_elementos = (1, 1, 1, 1, 3)
chequeo = [elemento == 1 for elemento in mis_elementos]
print(chequeo)

# Uso de SUM para hacer los mismo que ALL. True = 1, False = 0.
if sum(chequeo) == len(chequeo):
    print(True)
print(False)


# Concatenación de Tuplas:
tupla_1 = ('hola', 'mundo')
tupla_2 = ('adiós', 'mundo')
print(tupla_1 + tupla_2)


# Tuplas y numeros:
numeros = (2, 4, 8, 1, 5)
print('números ', numeros)
print('mínimo', min(numeros))
print('máximo ', max(numeros))
print('suma', sum(numeros))
print('orden ', sorted(numeros))
print('orden inverso ', sorted(numeros, reverse=True))
