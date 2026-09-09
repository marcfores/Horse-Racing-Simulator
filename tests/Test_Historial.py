import pytest
from Carrera_Caballos_Español import HistorialJuego

@pytest.fixture
def historial():
    historial = HistorialJuego("test_historial.txt")
    yield historial
    # No se puede limpiar el historial si no hay método definido en la clase

def test_mostrar_historial_vacio(capsys, historial):
    historial.mostrar_historial()
    captured = capsys.readouterr()
    assert "El historial está vacío." in captured.out


def test_agregar_puntuacion(historial):
    historial.agregar_puntuacion("Jugador1", 100)
    assert historial.puntuaciones_jugadores["Jugador1"] == 100

def test_agregar_puntuacion_existente(historial):
    historial.agregar_puntuacion("Jugador1", 200)
    assert historial.puntuaciones_jugadores["Jugador1"] == 300

def test_mostrar_historial_con_datos(capsys, historial):
    historial.agregar_puntuacion("Jugador2", 300)
    historial.agregar_puntuacion("Jugador3", 400)
    historial.mostrar_historial()
    captured = capsys.readouterr()
    assert "Jugador2: 300" in captured.out
    assert "Jugador3: 400" in captured.out

def test_guardar_historial(historial):
    historial.agregar_puntuacion("Jugador4", 500)


if __name__ == "__main__":
    pytest.main([__file__])
