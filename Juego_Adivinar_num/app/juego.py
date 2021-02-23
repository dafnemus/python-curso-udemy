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

    def adivinar_num(self) -> bool:
        while self.intentos <= 7:
            numero = int(input('numero: '))
            if numero == self.num_secret:
                print(f'Gano el numero era {self.num_secret}')
                break
            if numero < self.num_secret:
                print('Numero chico')
            else:
                print('Numero Grande')
            if self.intentos == 7:
                print(f'Perdiste era el: {self.num_secret}')
            self.intentos += 1


juego = Juego()
juego.adivinar_num()
