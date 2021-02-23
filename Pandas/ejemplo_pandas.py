# pylint: disable=missing-docstring

import pandas as pd

lenguajes = pd.read_csv('Pandas/lenguajes.csv')

print(lenguajes)

print()
print('lenguajes es de tipo:  ', type(lenguajes))

print()
descripcion = lenguajes.describe()
print(descripcion)

print()
# Extracción de una serie:
nombre_serie = lenguajes['Nombre']
print(nombre_serie)

print(type(nombre_serie))
print()

# Ultimo año en la tabla:

ultimo_año = lenguajes['Año'].max()
print(ultimo_año)

print()
# Primer año en la tabla:
primer_año = lenguajes['Año'].min()
print(primer_año)

print()

# Lenguajes después de 1990

mas_actuales = lenguajes[lenguajes['Año'] > 1990]
print(mas_actuales)

# imprimir solo los nombres de los lenguajes despues de 1990

actuales = mas_actuales['Lenguaje'].to_dict()
print(actuales)
