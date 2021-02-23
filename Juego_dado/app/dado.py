# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random


class IngresoError(ValueError):
    pass


class Dado:
    def __init__(self):
        self.caras = random.randint(1, 6)

    def adivinar_numero(self, numero: int) -> bool:
        if not isinstance(numero, int):
            raise IngresoError()
        if numero == self.caras:
            return 'Acerto'
        if numero < 1 or numero > 6:
            return 'Numero fuera de rango'
        return 'No acertó'
