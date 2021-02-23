# pylint: disable=missing-docstring
frutas = []


# Lectura de archivo
with open('Unidad_9/frutas.txt', 'r') as f:
    frutas = f.readlines()
    print(frutas)

    frutas = [fruta.rstrip() for fruta in frutas]
    print(frutas)


# Escritura de archivo:
with open('Unidad_9/lista_actual_frutas.txt', 'w') as f:
    frutas.append('Papaya')
    for index, _ in enumerate(frutas):
        frutas[index] = frutas[index].upper() + '\n'
    f.writelines(frutas)
