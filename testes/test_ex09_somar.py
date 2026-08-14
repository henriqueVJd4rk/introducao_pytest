from ex09_somar import somar

def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-2, -3) == -5

def test_somar_zero():
    assert somar(10, 0) == 10
