# pylint: disable=missing-docstring

# aplicando Diccionarios a ambientes reales.

# diciionario e pokemon:
from urllib.request import urlopen
from PIL import Image
import requests


POKEMON = 'https://pokeapi.co/api/v2/pokemon/pikachu'
result = requests.get(POKEMON)
pk_data = result.json()
name = pk_data['name']
image_pk = pk_data['sprites']['front_default']
print(f'Pokemon: {name}')
print(f'imagen de frente: {image_pk}')


def desplegar_imagen(url):
    img = Image.open(urlopen(url))
    return img


imagen = desplegar_imagen(image_pk)
print(imagen)
