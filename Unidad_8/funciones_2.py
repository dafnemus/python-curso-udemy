# pylint: disable=missing-docstring

from urllib.request import urlopen
from PIL import Image
import requests

# Api Dog.
API_DOG = 'https://dog.ceo/api/breeds/image/random'


def display_image(url):
    imagen = Image.open(urlopen(url))
    return imagen


def get_json(api_url):
    return requests.get(api_url).json()


foto_perro = get_json(API_DOG)['message']  # Devuelve una imagen
print(foto_perro)

print(display_image(foto_perro))
display_image(foto_perro).show()  # Muestro imagen.

# generar 3 imagenes nuevas y guardalas en una lista.

perros = []
for _ in range(3):
    perros.append(get_json(API_DOG)['message'])

print(perros)

# Mostrar las imagenes de la lista perros:

for i in perros:
    display_image(i).show()
