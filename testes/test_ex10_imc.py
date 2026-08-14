from ex10_imc import calcular_imc
import pytest

def test_imc_basico():
    assert calcular_imc(70, 1.75) == pytest.approx(22.8571, rel=1e-4)

def test_imc_outro_valor():
    assert calcular_imc(60, 1.60) == pytest.approx(23.4375)

def test_altura_zero():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)
