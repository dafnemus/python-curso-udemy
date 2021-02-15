# pylint: disable=missing-docstring
from app.juego import Juego, NoHayImpostor, IngresoError
import pytest


def test_impostor_encontrado():
    jugadores = ['True', 'False', 'False']
    juego = Juego(jugadores)
    assert juego.encontrar_impostor() == 'El impostor está en la posición 0'


def test_impostor_no_esta():
    jugadores = ['False', 'False', 'False']
    with pytest.raises(NoHayImpostor):
        Juego(jugadores)


def test_ingreso_jugadores_error():
    jugadores = 22
    with pytest.raises(IngresoError):
        Juego(jugadores)


def test_no_puede_haber_2_impostores():
    jugadores = ['True', 'True', 'False']
    with pytest.raises(IngresoError):
        Juego(jugadores)
