import pytest
from Carrera_Caballos_Español import Caballo


def test_creacion_caballo():
    caballo = Caballo("Caballito", "Rápido")
    assert caballo.nombre == "Caballito"
    assert caballo.tipo == "Rápido"


def test_dibujar_caballo():
    caballo = Caballo("Caballito", "Fuerte")
    assert caballo.dibujar_caballo() == "🐎"


def test_elegir_tipo_caballo(mocker, monkeypatch):
    # Mock input para simular la entrada del usuario
    mocker.patch('builtins.input', side_effect=["2"])  # Simula la selección 'Rápido'

    # Prueba la función elegir_tipo_caballo
    tipo_seleccionado = Caballo.elegir_tipo_caballo()
    assert tipo_seleccionado == "Rápido"

    # Prueba de selección inválida
    mocker.patch('builtins.input', side_effect=["1"])  # Simula selecciones inválidas seguidas de válida
    tipo_seleccionado = Caballo.elegir_tipo_caballo()
    assert tipo_seleccionado == "Normal"


def test_elegir_tipo_caballo_con_input_invalido(mocker):
    # Simula input no numérico seguido de input numérico válido
    mocker.patch('builtins.input', side_effect=["a", "2"])
    tipo_seleccionado = Caballo.elegir_tipo_caballo()
    assert tipo_seleccionado == "Rápido"
