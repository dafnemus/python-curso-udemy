# Adivinar un núemro random en menos de 7 intentos.
# el usuario debe ingresar el num
# Darle pistas al usuario.

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random


class Juego:
    def __init__(self):
        self.num_secret = random.randint(0, 10)
        self.intentos = 0

    def adivinar_num(self):
        while self.intentos <= 7:
            numero = int(input('numero: '))
            if numero == self.num_secret:
                print('Gano')
                break
            if numero < self.num_secret:
                print('Numero chico')
            else:
                print('Numero Grande')
            self.intentos += 1
        if self.intentos == 7:
            print('Perdiste')


juego = Juego()
juego.adivinar_num()
