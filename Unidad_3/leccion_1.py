# pylint: disable=missing-docstring
nombre = input('Hola, Cuál es tu nombre?: ')
print(f'Hola {nombre}')  # formato 1

print('Hola', end=' ')  # formato 2
print(nombre)

# conversión de horas a segundos.
horas = int(input('Ingrese cantidad de Horas: '))
UN_SEGUNDO = 3600
segundos_totales = horas * UN_SEGUNDO
print(f'segundos {segundos_totales}')

# conversion de Celsius a Farenheit.
# formula (0 °C × 9/5) + 32 = 32 °F

celsius = int(input('Ingrese cantidad de grados Celsius: '))
VALOR_FARENHEIT = 32
farenheits = (celsius * 9/5) + VALOR_FARENHEIT
print(f'{farenheits}° F')
