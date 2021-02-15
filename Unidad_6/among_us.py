# Siguiendo la logica del Among Us, buscar el impostor.
# el impostor = True
# Determinar la posición del impostor.

list_crew = ['True', 'False', 'False']
list_crew = [True if b.strip() == 'True' else False for b in list_crew]

# TODO: your code starts here
for i in range(len(list_crew)):
    if list_crew[i] == True:
        print('El impostor está en la posición', i)
