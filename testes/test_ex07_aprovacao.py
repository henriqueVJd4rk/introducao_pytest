from ex07_aprovacao import verificar_aprovacao

def test_aprovado():
    assert verificar_aprovacao(7) == "Aprovado"

def test_recuperacao():
    assert verificar_aprovacao(6.5) == "Recuperação"

def test_reprovado():
    assert verificar_aprovacao(4.9) == "Reprovado"
