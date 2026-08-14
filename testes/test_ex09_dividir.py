from ex09_dividir import dividir
import pytest

def test_dividir_exato():
    assert dividir(6, 2) == 3

def test_dividir_com_decimal():
    assert dividir(5, 2) == 2.5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)
