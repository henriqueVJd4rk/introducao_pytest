from ex13_contagem_regressiva import contagem_regressiva

def test_contagem_regressiva(capsys):
    contagem_regressiva(3)
    assert capsys.readouterr().out == "3\n2\n1\n0\n"

def test_contagem_a_partir_de_um(capsys):
    contagem_regressiva(1)
    assert capsys.readouterr().out == "1\n0\n"

def test_contagem_a_partir_de_zero(capsys):
    contagem_regressiva(0)
    assert capsys.readouterr().out == "0\n"
