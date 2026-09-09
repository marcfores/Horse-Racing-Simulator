import pytest
from Carrera_Caballos_Español import EntrenamientoCaballos

def test_creacion_entrenamiento_caballos():
    jugadores = ["Jugador1", "Jugador2"]
    entrenamiento = EntrenamientoCaballos(jugadores)
    assert entrenamiento.jugadores == jugadores

def test_entrenamiento_preguntas_respuestas(monkeypatch, capsys):
    respuestas = iter(["Marrón", "Perro", "Lobo", "Yegua", "Potro"])

    def mock_input(prompt):
        return next(respuestas)

    monkeypatch.setattr('builtins.input', mock_input)

    entrenamiento = EntrenamientoCaballos(["Jugador1"])
    entrenamiento.entrenamiento_preguntas_respuestas()

    captured = capsys.readouterr()
    assert "Entrenamiento completado!" in captured.out

def test_otro_juego_entrenamiento(monkeypatch, capsys):
    alturas = iter([3, 4, 2, 1, 5])

    def mock_input(prompt):
        return str(next(alturas))

    monkeypatch.setattr('builtins.input', mock_input)

    entrenamiento = EntrenamientoCaballos(["Jugador1"])
    entrenamiento.otro_juego_entrenamiento()

    captured = capsys.readouterr()
    assert "Juego completado!" in captured.out
