notas = []
while True:
    entrada = input("Digite a nota (0-10) ou 'fim' para encerrar: ").lower()

    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nA média da turma é: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")