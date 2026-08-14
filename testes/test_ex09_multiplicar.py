from ex09_multiplicar import multiplicar

def test_multiplicar_positivos():
    assert multiplicar(2, 3) == 6

def test_multiplicar_por_zero():
    assert multiplicar(8, 0) == 0

def test_multiplicar_negativos():
    assert multiplicar(-2, 3) == -6
