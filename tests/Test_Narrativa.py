import pytest
from Carrera_Caballos_Español import NarrativaJuego

def test_mostrar_evento(capsys):
    # Creamos una instancia de NarrativaJuego
    narrativa = NarrativaJuego()

    # Probamos la función mostrar_evento
    narrativa.mostrar_evento()

    # Capturamos la salida estándar para realizar aserciones
    captured = capsys.readouterr()

    # Verificamos que la salida no esté vacía
    assert captured.out != ""

    # Dado que el evento es aleatorio, no podemos predecir la salida exacta
    # Podemos realizar aserciones para verificar que la salida no esté vacía, pero no verificar el contenido específico