from ex14_desconto import calcular_desconto

def test_desconto_dez_porcento():
    assert calcular_desconto(100, 10) == 90

def test_desconto_cinquenta_porcento():
    assert calcular_desconto(200, 50) == 100

def test_sem_desconto():
    assert calcular_desconto(80, 0) == 80
