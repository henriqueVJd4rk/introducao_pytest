from ex20_cadastrar_produto import cadastrar_produto

def test_produto_formatado(capsys):
    cadastrar_produto("Mouse Gamer", 89.90, 15)
    saida = capsys.readouterr().out
    assert "Produto: Mouse Gamer" in saida
    assert "Preço: R$ 89.90" in saida
    assert "Estoque: 15 unidades" in saida

def test_outro_produto(capsys):
    cadastrar_produto("Teclado", 120, 5)
    saida = capsys.readouterr().out
    assert "Produto: Teclado" in saida

def test_preco_com_duas_casas(capsys):
    cadastrar_produto("Cabo", 12.5, 10)
    saida = capsys.readouterr().out
    assert "Preço: R$ 12.50" in saida
