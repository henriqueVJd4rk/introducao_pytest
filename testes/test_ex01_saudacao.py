from ex01_saudacao import saudacao

def test_saudacao_nome_comum():
    assert saudacao("João") == "Olá, João! Seja bem-vindo."

def test_saudacao_outro_nome():
    assert saudacao("Maria") == "Olá, Maria! Seja bem-vindo."

def test_saudacao_nome_vazio():
    assert saudacao("") == "Olá, ! Seja bem-vindo."
