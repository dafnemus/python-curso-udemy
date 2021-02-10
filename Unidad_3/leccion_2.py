# pylint: disable=missing-docstring

# determinar si un numero es par o no.
numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    print(f'Es par {numero}')
else:
    print(f'Es impar {numero}')
