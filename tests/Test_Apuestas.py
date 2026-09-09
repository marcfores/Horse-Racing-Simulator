import pytest
from Carrera_Caballos_Español import Apuestas
from _pytest.monkeypatch import MonkeyPatch

def test_realizar_apuestas(monkeypatch):
    # Creamos una instancia de Apuestas
    apuestas = Apuestas(["Jugador1", "Jugador2"], monedas_disponibles=100)
    
    # Simulamos la entrada de usuario para realizar apuestas
    monkeypatch.setattr('builtins.input', lambda _: '20')  # Simulamos una apuesta de 20 monedas para Jugador1
    apuestas.realizar_apuestas()
    
    assert apuestas.apuestas["Jugador1"] == 20
    assert apuestas.monedas_disponibles == 80  # Verificamos que las monedas disponibles se redujeron correctamente
    
    # Probamos otra apuesta para el Jugador2
    monkeypatch.setattr('builtins.input', lambda _: '30')  # Simulamos una apuesta de 30 monedas para Jugador2
    apuestas.realizar_apuestas()
    
    assert apuestas.apuestas["Jugador2"] == 30
    assert apuestas.monedas_disponibles == 50  # Verificamos que las monedas disponibles se redujeron correctamente

def test_obtener_ganadores():
    # Creamos una instancia de Apuestas
    apuestas = Apuestas(["Jugador1", "Jugador2"], monedas_disponibles=100)
    # Establecemos las apuestas
    apuestas.apuestas = {"Jugador1": 20, "Jugador2": 30}
    
    # Probamos obtener los ganadores cuando el ganador es Jugador1
    ganadores_jugador1 = apuestas.obtener_ganadores("Jugador1")
    assert ganadores_jugador1 == [("Jugador1", 20)]
    
    # Probamos obtener los ganadores cuando no hay ganadores
    ganadores_ninguno = apuestas.obtener_ganadores("Jugador3")  # Un jugador que no está en la lista de apuestas
    assert ganadores_ninguno == []

    # Probamos obtener los ganadores cuando todos los jugadores apostaron al mismo ganador
    apuestas.apuestas = {"Jugador1": 20, "Jugador2": 30}
    ganadores_jugador2 = apuestas.obtener_ganadores("Jugador2")
    assert ganadores_jugador2 == [("Jugador2", 30)]