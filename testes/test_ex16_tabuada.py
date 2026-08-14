from ex16_tabuada import tabuada

def test_tabuada_de_cinco(capsys):
    tabuada(5)
    saida = capsys.readouterr().out
    assert "5 x 1 = 5" in saida
    assert "5 x 10 = 50" in saida

def test_tabuada_de_dois(capsys):
    tabuada(2)
    saida = capsys.readouterr().out
    assert "2 x 5 = 10" in saida

def test_tabuada_tem_dez_linhas(capsys):
    tabuada(3)
    saida = capsys.readouterr().out
    assert len(saida.strip().splitlines()) == 10
