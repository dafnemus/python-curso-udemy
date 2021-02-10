# pylint: disable=missing-docstring
nombre = input('Hola, Cuál es tu nombre?: ')
print(f'Hola {nombre}')  # formato 1

print('Hola', end=' ')  # formato 2
print(nombre)

# conversión de horas a segundos.
horas = int(input('Ingrese cantidad de Horas: '))
UN_SEGUNDO = 3600
segundos_totales = horas * UN_SEGUNDO
