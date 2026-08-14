from ex03_par_impar import eh_par

def test_numero_par():
    assert eh_par(8) is True

def test_numero_impar():
    assert eh_par(7) is False

def test_zero_e_par():
    assert eh_par(0) is True
