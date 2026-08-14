from calculadora import somar, subtrair, dividir, multiplicar

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(2, 3) == -1

def test_multiplicar():
    assert multiplicar(2, 3) == 6

def test_dividir():
    assert dividir(3, 3) == 1