# pylint: disable=missing-docstring

# Crear una funcion que diga: Hola y salude a una persona


def saludar(name=''):
    print('Hola', name)


saludar()


saludar('marta')

vocales = {}


def contar_vocales(nombre):
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
