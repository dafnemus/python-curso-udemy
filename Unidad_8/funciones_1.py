# pylint: disable=missing-docstring

# Crear una funcion que diga: Hola y salude a una persona


def saludar(name: str) -> str:
    print('Hola', name)


saludar('marta')

vocales = {}


def contar_vocales(nombre: str) -> dict:
    nombre = nombre.lower()

    for vocal in 'aeiou':
        contador = nombre.count(vocal)
        vocales[vocal] = contador

    return vocales.items()


contar_vocales('lola')


nombres = ['luis', 'pablo', 'lola', 'julieta']
for persona in nombres:
    dict_vocal = contar_vocales(persona)
    print(f'vocales {persona}: {dict_vocal}')

# Funcion Par usando pistas:


def es_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    return False


es_par(2)

# seber si es par dentro de un rango:

for num in range(2, 10):
    print(num, es_par(num))
