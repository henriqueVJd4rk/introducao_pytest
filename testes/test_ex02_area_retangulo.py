from ex02_area_retangulo import calcular_area

def test_area_inteiros():
    assert calcular_area(5, 4) == 20

def test_area_com_zero():
    assert calcular_area(10, 0) == 0

def test_area_decimal():
    assert calcular_area(2.5, 4) == 10
