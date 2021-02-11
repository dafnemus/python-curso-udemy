# pylint: disable=missing-docstring
# 1. Aplica un incremento de sueldo del 8% al salario de un trabajador.
# Para ello, recuerda que primero debes solicitar el monto base del salario.

def incrementar_sueldo(sueldo):
    incremento = 0.08
    valor_incrementado = sueldo * incremento
    sueldo_incrementado = sueldo + valor_incrementado
    print(f'Total sueldo:{sueldo_incrementado}', end=' ')
    print(f'incremento: {valor_incrementado}')


incrementar_sueldo(2000)

# 2. Aplica un incremento de sueldo del 8% al salario de un trabajador,
# solo si este gana menos que el salario mínimo
# (escoge cualquier valor para el salario mínimo, porejemplo 1000).
# Si el trabajador gana más que el salario mínimo, el incremento es del 5%


def incrementar_sueldo_2(sueldo):
    sueldo_minimo = 1000
    incremento_1 = 0.08
    incremento_2 = 0.05
    sueldo_incrementado = 0
    valor_incrementado = 0
    if sueldo <= sueldo_minimo:
        valor_incrementado = sueldo * incremento_1
    elif sueldo > sueldo_minimo:
        valor_incrementado = sueldo * incremento_2
    sueldo_incrementado = sueldo + valor_incrementado

    print(f'Total sueldo:{sueldo_incrementado}', end=' ')
    print(f'incremento: {valor_incrementado}')


incrementar_sueldo_2(800)
incrementar_sueldo_2(2000)


# 3. Dado un valor que representa una cantidad en segundos,
# indica su equivalente en minutos, horas y días.

def convertir_segundos(segundos):
    un_minuto = 60
    hora = 3600
    dias = 86400

    resultado_min = segundos / un_minuto
    resultado_hr = segundos / hora
    resultado_dia = segundos / dias

    print(f'segundos {segundos}')
    print(f'segundos a hora: {resultado_hr}')
    print(f'segundos a minutos: {resultado_min}')
    print(f'segundosa dias: {resultado_dia}')


convertir_segundos(87600)
