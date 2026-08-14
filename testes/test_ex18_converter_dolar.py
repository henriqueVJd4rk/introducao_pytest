from ex18_converter_dolar import converter_dolar
import pytest

def test_converter_100_reais():
    assert converter_dolar(100, 5) == 20

def test_converter_250_reais():
    assert converter_dolar(250, 5) == 50

def test_cotacao_zero():
    with pytest.raises(ValueError):
        converter_dolar(100, 0)
