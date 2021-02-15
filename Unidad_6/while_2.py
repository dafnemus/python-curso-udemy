# pylint: disable=missing-docstring

# Prćtica de WHILE, BREAK, CONTINUE.

# 1. Usar while para imprimir del 0 al 1.
INDEX = 0
while INDEX < 2:
    print(f'index {INDEX}')
    INDEX += 1
print('end')

print()
# 2. Usar while para imprimir de 0 al 10
INDEX = 0
while INDEX <= 10:
    print(f'INDEX {INDEX}')
    INDEX += 1
print('end')

print()
# 3. Usando BREAK para romper la condicion del WHILE.
while True:
    print('*', end='-')
    break  # la condición se repetirá 1 vez.

print()

# 4. WHILE, BREAK hasta cumplir un IF.
INDEX = 0
while True:
    print(f'index {INDEX}')
    INDEX += 1
    if INDEX == 2:
        break
print('end')

# 4. WHILE, uso del CONTINUE.
INDEX = 0
while INDEX < 5:
    print(f'INDEX {INDEX}', end=' - ')
    INDEX += 1
    if INDEX >= 3:
        print()
        continue
    print(f'INDEX despues: {INDEX}')
print('end')

print()

# 5. WHILE y listas usando pop().

nombres = ['lola', 'lila', 'lucas', 'pablo']

while nombres:
    print(nombres, end='-> ')
    nombres.pop()
    print(f'version nueva {nombres}')
print('end')

print()

# 6. WHILE en una linea. Ejemplo:
# while VALUE < 5: VALUE += 1; print(f'INDEX {VALUE}')

# 7. imprimir la tabla del 12.
VALOR_1 = 1
VALOR_2 = 1

while VALOR_1 <= 12:
    while VALOR_2 <= 12:
        MULTIPLICACION = VALOR_1 * VALOR_2
        print(f'{VALOR_1}X{VALOR_2} = {MULTIPLICACION}')
        VALOR_2 += 1
    VALOR_2 = 1
    VALOR_1 += 1
