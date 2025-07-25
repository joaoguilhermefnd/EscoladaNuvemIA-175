# Define o valor de PI com a precisão especificada
PI = 3.14159265

# Solicita o valor do raio ao usuário
# Converte a entrada para um número de ponto flutuante
raio = float(input("Digite o valor do raio da circunferência: "))

# --- Lógica de Validação e Cálculo com if/else ---
# Verifica se o raio é um valor válido (não pode ser negativo)
if raio >= 0:
    # Se o raio for válido, calcula a área
    # A fórmula é: area = PI * (raio elevado ao quadrado)
    area = PI * (raio ** 2)

    # Imprime a mensagem "A=" seguida pelo valor da área, formatado para 4 casas decimais
    print(f"A={area:.4f}")
else:
    # Se o raio for negativo, imprime uma mensagem de erro
    print("Erro: O raio não pode ser um valor negativo. Por favor, digite um valor válido.")