import pytest
import random
from Carrera_Caballos_Español import ObstaculoPotenciador

@pytest.fixture
def evento():
    return ObstaculoPotenciador()

def test_generar_evento(evento):
    evento_generado = evento.generar_evento()
    assert evento_generado in ["¡Has encontrado un obstáculo! Tu caballo se ha ralentizado.", 
                               "¡Has encontrado un potenciador! Tu caballo se ha acelerado."]

if __name__ == "__main__":
    pytest.main([__file__])
