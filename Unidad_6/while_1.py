# pylint: disable=missing-docstring

# Consideraciones con las itercaiones. Ejemplos:

# No se cumple la condicion. Imprime: end while
VALUE = 0
while VALUE > 1:
    VALUE *= 2
    print(f'value {VALUE}')
print('end while')

print()
# OJO: ciclo infinito. Uso del break para terminarlo.
VALUE = 2
while VALUE > 1:
    VALUE *= 2
    print(f'value {VALUE}')
    break
print('end while')

print()

# Uso de else en el while. Raro, pero existe.
VALUE = 1
while VALUE <= 1:
    VALUE *= 2
    print(f'value {VALUE}')
else:  # pylint: disable=W0120
    print('end while')
