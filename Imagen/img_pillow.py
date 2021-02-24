# pylint: disable=missing-docstring

import sys
# Manejo de imagenes:
from PIL import Image, ImageDraw, ImageFont

# find a font file

GATO = 'Imagen/cat1.jpg'

try:
    imagen = Image.open(GATO)
except IOError:
    print('error de carga de imagen')
    sys.exit(1)

imagen.show()

# dibuja TEXTo en la imagen
idraw = ImageDraw.Draw(imagen)
TEXT = "Gatito Michifus"

# FUENTE para la imagen
FUENTE = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
font = ImageFont.truetype(FUENTE, size=36)
idraw.TEXT((150, 180), TEXT, font=font)

imagen.show()
