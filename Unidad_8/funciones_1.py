# pylint: disable=missing-docstring

# Crear una funcion que diga: Hola y salude a una persona


def saludar(name=''):
    print('Hola', name)


saludar()


saludar('marta')

vocales = dict()


def contar_vocales():
    nombre_original = input('Tu nombre es: ')
    nombre = nombre_original.lower()

    for vocal in 'aeiou':
        contador = nombre.count(vocal)
        vocales[vocal] = contador

    print(f'vocales: {vocales.items()}')


contar_vocales()
