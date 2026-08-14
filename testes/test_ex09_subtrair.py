from ex09_subtrair import subtrair

def test_subtrair_positivos():
    assert subtrair(8, 3) == 5

def test_subtrair_resultado_negativo():
    assert subtrair(3, 8) == -5

def test_subtrair_zero():
    assert subtrair(10, 0) == 10
