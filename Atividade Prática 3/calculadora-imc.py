# Solicita o peso do usuário em quilogramas
# Converte a entrada para um número de ponto flutuante, pois o peso pode ter decimais
peso = float(input("Digite seu peso em kg (ex: 70.5): "))

# Solicita a altura do usuário em metros
# Converte a entrada para um número de ponto flutuante, pois a altura pode ter decimais
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# Calcula o IMC (Índice de Massa Corporal)
# A fórmula é peso / (altura * altura) ou peso / (altura ** 2)
imc = peso / (altura ** 2)

# Classifica o IMC de acordo com a tabela padrão
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:  # Para todos os outros cenários (IMC >= 30)
    classificacao = "Obeso"

# Exibe o IMC calculado e a classificação
# O imc:.2f formata o IMC para duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")