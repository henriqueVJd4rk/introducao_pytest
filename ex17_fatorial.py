def fatorial(numero):
    if numero < 0 or int(numero) != numero:
        raise ValueError("O número deve ser um inteiro não negativo.")
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado
