def validar_senha(senha):
    if len(senha) >= 8:
        return "Senha válida"
    return "Senha inválida"
