# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

# Clases; Ejemplo: Lista de Perros.


class Perro:
    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info_perro(self):
        info = f'perro: {self.nombre}, raza: {self.raza}'
        return info


lista_perros = []
perro_1 = Perro('toto', 'caniche')
lista_perros.append(perro_1)
perro_2 = Perro('capitan', 'maltes')
lista_perros.append(perro_2)

for i in lista_perros:
    perro = i.mostrar_info_perro()
    print(perro)
