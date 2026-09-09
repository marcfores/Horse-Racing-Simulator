import pytest
import random
from Carrera_Caballos_Español import CajaSorpresa

def test_creacion_caja_sorpresa():
    caja = CajaSorpresa()
    assert isinstance(caja, CajaSorpresa)

def test_canjear_caja_sorpresa(mocker):
    # Mock de random.choice para simular la selección aleatoria de eventos
    eventos_mock = ["Evento 1", "Evento 2", "Evento 3"]
    mocker.patch('random.choice', return_value="Evento 2")

    caja = CajaSorpresa()
    resultado = caja.canjear()
    assert resultado == "Evento 2"

def test_canjear_caja_sorpresa_multiple(mocker):
    # Mock de random.choice para simular múltiples selecciones aleatorias
    eventos_mock = ["Evento 1", "Evento 2", "Evento 3"]
    mocker.patch('random.choice', side_effect=["Evento 1", "Evento 3", "Evento 1"])

    caja = CajaSorpresa()
    resultados = [caja.canjear() for _ in range(3)]
    assert resultados == ["Evento 1", "Evento 3", "Evento 1"]
