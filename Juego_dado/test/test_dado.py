# pylint: disable=missing-docstring
from app.dado import Dado, IngresoError
import pytest


def test_adivinar_numero_fuera_de_rango():
    dado = Dado()
    resultado = dado.adivinar_numero(7)
    assert resultado == 'Numero fuera de rango'


def test_validar_numero():
    dado = Dado()
    with pytest.raises(IngresoError):
        dado.adivinar_numero('7')
