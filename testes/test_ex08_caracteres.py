from ex08_caracteres import contar_caracteres

def test_contagem_texto():
    assert contar_caracteres("Python") == 6

def test_contagem_com_espacos():
    assert contar_caracteres("Olá mundo") == 9

def test_string_vazia():
    assert contar_caracteres("") == 0
