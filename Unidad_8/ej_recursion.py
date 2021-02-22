# pylint: disable=missing-docstring
# Hacer el conteo regresivo de una nave espacial:
# Usar recursión


def despegar(numero: int):
    if numero == 0:
        print('Despegue')
    else:
        print(numero)
        despegar(numero-1)


despegar(5)
