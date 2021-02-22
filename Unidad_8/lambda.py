# pylint: disable=missing-docstring

# Lambda: funciones anonimas.
doble = lambda num: num * 2  # noqa: E731
RESULTADO = doble(8)
print(RESULTADO)


lista = range(1, 10, 2)
nueva_lista = list(map(lambda x : pow(x, 2), lista))
print(nueva_lista)

numeros = range(1, 10)
multiplos = list(filter(lambda x: (x % 2 == 0), numeros))
print(multiplos)
