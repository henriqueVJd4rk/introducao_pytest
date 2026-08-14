# 1 - Saudação Personalizada
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo."


# 2 - Área do Retângulo
def calcular_area(base, altura):
    return base * altura


# 3 - Número Par ou Ímpar
def eh_par(numero):
    return numero % 2 == 0


# 4 - Maior de Dois Números
def maior_numero(a, b):
    return max(a, b)


# 5 - Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 6 - Média
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# 7 - Aprovação
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


# 8 - Contar Caracteres
def contar_caracteres(texto):
    return len(texto)


# 9 - Calculadora
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


# 10 - IMC
def calcular_imc(peso, altura):
    return peso / altura ** 2


# 11 - Classificação de Número
def classificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"


# 12 - Potência
def potencia(base, expoente):
    return base ** expoente


# 13 - Contagem Regressiva
def contagem_regressiva(inicio):
    lista = []

    for i in range(inicio, -1, -1):
        lista.append(i)

    return lista


# 14 - Desconto
def calcular_desconto(valor, percentual):
    return valor - (valor * percentual / 100)


# 15 - Vogais
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)


# 16 - Tabuada
def tabuada(numero):
    resultado = []

    for i in range(1, 11):
        resultado.append(f"{numero} x {i} = {numero*i}")

    return resultado


# 17 - Fatorial
def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado


# 18 - Conversão de Moedas
def converter_dolar(valor_reais, cotacao):
    return valor_reais / cotacao


# 19 - Validação de Senha
def validar_senha(senha):
    tem_letra = any(letra.isalpha() for letra in senha)
    tem_numero = any(numero.isdigit() for numero in senha)

    if len(senha) >= 8 and tem_letra and tem_numero:
        return "Senha válida"

    return "Senha inválida"


# 20 - Cadastro Produto
def cadastrar_produto(nome, preco, estoque):
    return (
        f"Produto: {nome}\n"
        f"Preço: R$ {preco:.2f}\n"
        f"Estoque: {estoque} unidades"
    )