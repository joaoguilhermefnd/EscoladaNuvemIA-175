while True:
    senha = input("Digite sua senha (mínimo 8 caracteres, com pelo menos um número) ou 'sair' para encerrar: ")

    if senha.lower() == 'sair':
        print("Saindo do verificador de senha.")
        break

    # Verifica o comprimento da senha
    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue

    # Verifica se a senha contém pelo menos um número
    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    # Se chegou aqui, a senha é forte
    print("Senha forte! Registrada com sucesso.")
    break