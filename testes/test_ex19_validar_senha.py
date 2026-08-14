from ex19_validar_senha import validar_senha

def test_senha_valida():
    assert validar_senha("abc12345") == "Senha válida"

def test_senha_invalida():
    assert validar_senha("1234567") == "Senha inválida"

def test_senha_com_oito_caracteres():
    assert validar_senha("abcdefgh") == "Senha válida"
