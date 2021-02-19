# pylint: disable=missing-docstring

'''
2. Escribe el nombre de al menos 8 personas que conozcas como elementos de una
lista (si no conoces tantas personas, no importa, inventa nombres). Una vez creada
la lista, aplica las siguientes operaciones:
a. Ordena los nombres en orden lexicográfico
b. Elimina a la persona con la que tengas menos afinidad, y construye la lista de
siete elementos.
'''

personas = ['lola', 'luna', 'carla', 'pablo', 'luis', 'pedro', 'maria', 'ana']

print(f'Personas: {personas}')
lista_ordenada = sorted(personas)

print(f'lista ordenada: {lista_ordenada}')

for persona in lista_ordenada:
    if persona == 'pablo':
        lista_ordenada.remove(persona)
print(f'lista sin pablo: {lista_ordenada}')
