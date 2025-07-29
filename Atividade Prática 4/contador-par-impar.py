pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").lower()

    if entrada == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print(f"\n--- Resumo ---")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")