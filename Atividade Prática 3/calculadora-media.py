# A entrada contém quatro números de ponto flutuante correspondentes às notas dos alunos.
# Usamos input().split() para ler a linha inteira e dividir em strings
# Depois, map(float, ...) converte cada string para float
n1, n2, n3, n4 = map(float, input().split())

# Define os pesos para cada nota
peso1 = 2
peso2 = 3
peso3 = 4
peso4 = 1

# Calcula a média ponderada
# Média = (Nota1*Peso1 + Nota2*Peso2 + Nota3*Peso3 + Nota4*Peso4) / (Soma dos Pesos)
media = (n1 * peso1 + n2 * peso2 + n3 * peso3 + n4 * peso4) / (peso1 + peso2 + peso3 + peso4)

# Imprime a média inicial, formatada com uma casa decimal
print(f"Media: {media:.1f}")

# --- Classificação do aluno ---

# Se a média for maior ou igual a 7.0, Aluno aprovado.
if media >= 7.0:
    print("Aluno aprovado.")
# Se a média calculada for inferior a 5.0, Aluno reprovado.
elif media < 5.0:
    print("Aluno reprovado.")
# Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, Aluno em exame.
else:  # Isso significa que a média está entre 5.0 e 6.9
    print("Aluno em exame.")

    # No caso do aluno estar em exame, lê a nota do exame.
    nota_exame = float(input())

    # Imprime a nota do exame digitada, formatada com uma casa decimal.
    print(f"Nota do exame: {nota_exame:.1f}")

    # Recalcula a média final (soma a pontuação do exame com a média anteriormente calculada e divide por 2).
    media_final = (media + nota_exame) / 2

    # Classifica o aluno após o exame:
    # "Aluno aprovado." (caso a média final seja 5.0 ou mais)
    if media_final >= 5.0:
        print("Aluno aprovado.")
    # "Aluno reprovado." (caso a média tenha ficado 4.9 ou menos).
    else:
        print("Aluno reprovado.")

    # Apresenta na última linha a mensagem "Media final: " seguido da média final para esse aluno.
    print(f"Media final: {media_final:.1f}")