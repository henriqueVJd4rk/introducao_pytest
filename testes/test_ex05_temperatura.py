from ex05_temperatura import celsius_para_fahrenheit

def test_zero_celsius():
    assert celsius_para_fahrenheit(0) == 32

def test_cem_celsius():
    assert celsius_para_fahrenheit(100) == 212

def test_trinta_celsius():
    assert celsius_para_fahrenheit(30) == 86
