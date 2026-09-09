import pytest
from Carrera_Caballos_Español import CarreraDeCaballos

@pytest.fixture
def carrera():
    return CarreraDeCaballos(["Jugador1", "Jugador2"])

def test_lanzar_dado():
    carrera = CarreraDeCaballos([])
    dado = carrera.lanzar_dado()
    assert dado >= 0 and dado <= 2

def test_jugar_turno(carrera):
    carrera.jugar_turno()
    assert all(posicion in range(0, 3) for posicion in carrera.posiciones.values())

def test_comprobar_ganador(carrera):
    carrera.posiciones["Jugador1"] = 20
    assert carrera.comprobar_ganador() == "Jugador1"

def test_mostrar_tablero(carrera):
    caballos_jugadores = {"Jugador1": "Normal", "Jugador2": "Normal"}
    carrera.mostrar_tablero(caballos_jugadores)

if __name__ == "__main__":
    pytest.main([__file__, "-s"])
