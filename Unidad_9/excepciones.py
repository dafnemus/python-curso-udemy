# pylint: disable=missing-docstring

# excepciones y archivos:
# Excepcion: Cuando se pasa un archivo erroneo
# TRY, EXCEPT, ELSE y FINALLY

LOCACION = 'Unidad_9/frutas.txt'
frutas = []
try:
    with open(LOCACION, 'r') as f_fruits:
        frutas = f_fruits.readlines()
except FileNotFoundError as error:
    print(error.strerror)
else:
    print('Todo OK')
finally:
    print('Siempre se va a ejecutar esto')

print(frutas)


# ASSERT:

NOTA = 22
try:
    if NOTA > 20:
        raise ValueError(f'la nota {NOTA} no puede ser mayor a 20')
except ValueError as error_ingreso:
    print('Error al ingresar la nota', error_ingreso)
