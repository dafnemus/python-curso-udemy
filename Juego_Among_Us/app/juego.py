# Siguiendo la logica del Among Us, buscar el impostor.
# el impostor = True
# Determinar la posición del impostor.

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods


class NoHayImpostor(ValueError):
    pass


class IngresoError(TypeError):
    pass


class Juego:
    def __init__(self, lista):
        self.lista = self.validar_jugadores(lista)

    def encontrar_impostor(self):
        for i in range(len(self.lista)):
            if self.lista[i] == 'True':
                return f'El impostor está en la posición {i}'
            return i

    def validar_jugadores(self, lista):
        if not isinstance(lista, list):
            raise IngresoError()
        if 'True' not in lista:
            raise NoHayImpostor()
        if lista.count('True') >= 2:
            raise IngresoError()
        self.lista = lista
        return self.lista
