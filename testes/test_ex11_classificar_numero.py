from ex11_classificar_numero import classificar_numero

def test_numero_positivo():
    assert classificar_numero(10) == "Positivo"

def test_numero_negativo():
    assert classificar_numero(-10) == "Negativo"

def test_numero_zero():
    assert classificar_numero(0) == "Zero"
