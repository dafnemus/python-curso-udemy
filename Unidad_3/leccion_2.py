# pylint: disable=missing-docstring

# determinar si un numero es par o no.
numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    print(f'Es par {numero}')
else:
    print(f'Es impar {numero}')

# determinar si es letra, digito o simbolo
caracter = input('ingrese un caracter: ')

if caracter.isalpha():
    print(f'{caracter} es letra')
elif caracter.isdigit():
    print(f'{caracter} es un digito')
else:
    print(f'{caracter} es un simbolo')
