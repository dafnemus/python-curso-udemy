# pylint: disable=missing-docstring

# Ejemplos de FOR y listas.

# Copiar una lista usando FOR.
lista_1 = [1, 2, 3]
lista_2 = []

for i in lista_1:
    lista_2.append(i)
print(lista_2)

lista_3 = lista_1.copy()
print(lista_3)

print()

# lisra de letras de una cadena.
PALABRA = 'hola'
letras = []
for letra in PALABRA:
    letras.append(letra)
print(letras)

# colocar los numeros par en una lista dentro del rango de N.

pares = []
for numin in range(11):
    if numin % 2 == 0:
        pares.append(numin)
print(pares)

# ahora con lista compresion
par = [num for num in range(8) if num % 2 == 0]
print(par)

# lista comprension usando if/else.

par_2 = [f'{num} par' if num % 2 == 0 else f'{num} impar' for num in range(8)]
print(par_2)
