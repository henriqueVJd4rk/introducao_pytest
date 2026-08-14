def converter_dolar(valor_reais, cotacao):
    if cotacao <= 0:
        raise ValueError("A cotação deve ser maior que zero.")
    return valor_reais / cotacao
