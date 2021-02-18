# pylint: disable=missing-docstring

# Stings, listas, Tuplas

# extraer un fragmento de u TEXTO.

TEXTO = '''
La nueva Filosofía.
Para Nietzsche la voluntad es la verdadera "esencia" de la realidad.
La realidad no es más que la expresión de la voluntad: ser es querer (...ser).
La realidad no es algo estático, permanente, inmutable; ni la consecuencia de algo estático, permanente, inmutable.
Siendo el fruto de la voluntad ha de ser multiforme y cambiante, como aquella.
La realidad es devenir, cambio, y no está sometida a otra determinación que a la de su propio querer.
Y el querer de la voluntad, al igual que el de todo lo real, es un querer libre, que rechaza toda determinación ajena a su propio devenir.

La voluntad, el querer, no se somete a lo querido, sino que se sobrepone a todos sus posibles objetos.
No quiere "esto" o "lo otro", sino sólo su propio querer.
Se trata de una voluntad libre y absoluta a la que Nietzsche denomina "voluntad de poder": es una voluntad vital, expansiva, dominante... una voluntad que se engendra a sí misma y que quiere su propio querer.
'''

print('Original: ', TEXTO)
# remover puntuacion y simbolos
TEXTO_2 = ''
PUNTUACION = '''¡!()-[]{};:'",<>./¿?@#$%^&*_~'''

for caracter in TEXTO:
    if caracter not in PUNTUACION:
        TEXTO_2 += caracter

print('TEXTO version 2: ', TEXTO_2)

# remover  los fin de linea.
TEXTO_2 = TEXTO_2.replace('\r', '').replace('\n', '').replace('\t', '')

print()
print('TEXTO version 3: ', TEXTO_2)

# contar caracteres:

print(f'caracteres totales: {len(TEXTO_2)}')

print()
# contar las palabras:
list_palabras = TEXTO_2.split()

print(f'palabras totales: {len(list_palabras)}')

# usar una tupla:
tupla_palabras = tuple(list_palabras)
print(tupla_palabras)

print()

# contar algún valor:
a = tupla_palabras.count('realidad')
o = tupla_palabras.count('voluntad')
print(f'realidad aparece: {a} veces')
print(f'voluntad aparece: {o} veces')

print()
# usando SET:
set_palabras = set(list_palabras)
print(set_palabras)

print(f'palabras totales con set: {len(set_palabras)}')

# usando otro set
mi_set = set(['la', 'es', 'el', 'de'])

print()
# union
print('union: ')
print(set_palabras.union(mi_set))

print()
# intersección
print('intersección')
print(set_palabras.intersection(mi_set))

print()
# diferancia
print('diferancia')
print(set_palabras.difference(mi_set))
print('palabras: ', len(set_palabras.difference(mi_set)))
