import pytest
import os
from Carrera_Caballos_Español import RankingJuego

@pytest.fixture
def ranking():
    ranking = RankingJuego("test_ranking.txt")
    yield ranking
    os.remove("test_ranking.txt") # Elimina el archivo creado después de las pruebas

def test_agregar_puntuacion(ranking):
    ranking.agregar_puntuacion("Jugador1", 100)
    assert ranking.puntuaciones_jugadores["Jugador1"] == 100

def test_obtener_ranking(ranking):
    ranking.agregar_puntuacion("Jugador2", 200)
    ranking.agregar_puntuacion("Jugador3", 300)
    assert ranking.obtener_ranking() == [("Jugador3", 300), ("Jugador2", 200)]

def test_guardar_ranking(ranking):
    ranking.agregar_puntuacion("Jugador4", 400)
    ranking.agregar_puntuacion("Jugador4", 2000) # Agrega una puntuación adicional para reflejar el cambio
    ranking.guardar_ranking()
    with open("test_ranking.txt", "r") as f:
        lines = f.readlines()
        assert len(lines) == 1
        assert lines[0] == "Jugador4:2400\n"

if __name__ == "__main__":
    pytest.main([__file__])
