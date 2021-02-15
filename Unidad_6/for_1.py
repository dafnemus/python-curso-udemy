# pylint: disable=missing-docstring

# Uso del FOR:

# Imprimir las letras de una cadena.
PALABRA = 'mañana'
for letra in PALABRA:
    print(letra)

print()

# imprimir los elementos de una lista.
lista_nombres = ['lola', 'pablo', 'matias']
for persona in lista_nombres:
    print(persona)

print()

# imprimir todad las letras de una lista
for palabra in lista_nombres:
    for letra in palabra:
        print(letra)

print()

# imprimir todos los numeros de una lista.
numeros = [1, 2, 3]
for num in numeros:
    print(num)

print()

# imprimir el rango de un numero.
for x in range(5):
    print(x)

print()
# imprimir el rango de un numero de 2 en 2.
for x in range(0, 10, 2):
    print(x)

print()
# FOR y break.
for x in range(0, 10, 2):
    print(x)
    if x == 4:
        break

print()
# FOR y continue imprimir as palbras sin A.
lista = ['ala', 'lupa', 'libro', 'a', 'pico']
for palabra in lista:
    if 'a' in palabra:
        continue
    print(palabra)

print()
