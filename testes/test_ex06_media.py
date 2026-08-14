from ex06_media import calcular_media

def test_media_inteiros():
    assert calcular_media(7, 8, 9) == 8

def test_media_com_decimais():
    assert calcular_media(5, 6, 7) == 6

def test_media_notas_iguais():
    assert calcular_media(10, 10, 10) == 10
