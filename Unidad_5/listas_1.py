# pylint: disable=missing-docstring
# crear una lista de números llamada list_number e imprimir el tipo de dato.
list_number = [2, 4, 5, 6, 7]

print(type(list_number))

# realizar una copia de la lista numeros y cambiar la primera posicion.

list_copia = list_number  # no recomendado. No realiza una copia.
list_copia[0] = 100

print(list_copia, list_number)

# imprimir el id de ambas listas.
print(id(list_number), id(list_copia))

print()
# Copiar una lista Metodo 1.
# realizar una copia de la lista numeros y cambiar la primera posicion.
# imprimir el id de ambas listas.

list_numero = [2, 3, 4, 5, 6, 7]
list_numero_copia = list_numero.copy()
list_numero_copia[0] = 100

print(f'list_numero: {list_numero}')
print(f'list_numero_copia: {list_numero_copia}')

print(f'id list_numero: {id(list_numero)}')
print(f'id list_numero_copia: {id(list_numero_copia)}')

print()
# Copiar una lista Metodo 2.
# realizar una copia de la lista numeros y cambiar la primera posicion.
# imprimir el id de ambas listas.

list_numero_2 = [2, 3, 4, 5, 6, 7]
list_numero_copia_2 = list_numero[:]
list_numero_copia_2[0] = 100

print(f'list_numero_2: {list_numero_2}')
print(f'list_numero_copia_2: {list_numero_copia_2}')

print(f'id list_numero_2: {id(list_numero_2)}')
print(f'id list_numero_copia_2: {id(list_numero_copia_2)}')

print()
# insertar un nuevo elemento.
lista = [1, 2, 3, 4, 5, 60]
lista.insert(5, 9)

print(f'lista: {lista}')

# remover un elemento.
lista.remove(3)
print(f'Lista con un elemento menos: {lista}')


# Buscar un elemento en una lista de nombres.

nombres = ['luis', 'pablo', 'lola', 'julieta']
luis = nombres.index('luis')
print(f'Luis esta en la posicion: {luis}')

print()

# convertir un string en una Lista.

COMIDA = 'arroz'
print(f'{COMIDA} es un: {type(COMIDA)}')

list_comida = list(COMIDA)
print(f'str: {COMIDA} a list: {list_comida}')

print(f'longitud de {list_comida}: {len(list_comida)}')
