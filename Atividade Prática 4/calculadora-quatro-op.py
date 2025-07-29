while True:
    try:
        num1_str = input("Digite o primeiro número: ")
        num1 = float(num1_str)

        num2_str = input("Digite o segundo número: ")
        num2 = float(num2_str)

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida. Tente novamente.")
                continue
            resultado = num1 / num2
        else:
            print("Erro: Operação inválida. Use +, -, * ou /. Tente novamente.")
            continue

        print(f"O resultado é: {resultado}")
        break  # Sai do loop se a operação for bem-sucedida

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar números válidos. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")