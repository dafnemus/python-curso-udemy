# pylint: disable=missing-docstring

'''
5. Un número capicúa es un número que se lee igual de izquierda a derecha, que de
derecha a izquierda (el equivalente a palíndromo pero para números). Escribe un
programa que determine si un número es capicúa o no.
'''

# 5:
numero = input('numero: ')

if numero[::-1] == numero:
    print('es capicua', int(numero))
else:
    print('no es capicua', int(numero))
