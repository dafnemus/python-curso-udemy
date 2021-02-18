# pylint: disable=missing-docstring

# aplicando Diccionarios a ambientes reales.

# diciionario e pokemon:
import webbrowser  # permite desplegar documentos basados en la web.
import requests

POKEMON = 'https://pokeapi.co/api/v2/pokemon'

webbrowser.open(POKEMON)

print(POKEMON)

# pokemon formato diccionario.
url_pokemon = f'{POKEMON}/?__a=1'
print(url_pokemon)

# obtener https de mi pokemon
result = requests.get(url_pokemon)
print(result)

# convertir a JSON
pk_data = result.json()

for key in pk_data.keys():
    print(key)

for key in pk_data['results']:
    print(key)

print(pk_data['results'][0]['name'])
