from ex15_vogais import contar_vogais

def test_contar_vogais():
    assert contar_vogais("Python") == 1

def test_contar_vogais_maiusculas():
    assert contar_vogais("AEIOU") == 5

def test_sem_vogais():
    assert contar_vogais("rhythms") == 0
