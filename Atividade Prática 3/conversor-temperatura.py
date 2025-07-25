# Solicita a temperatura ao usuário
temperatura = float(input("Digite a temperatura: "))

# Solicita a unidade de origem (C, F ou K)
# Converte para maiúscula para facilitar a comparação e evitar erros de digitação
unidade_origem = input("Unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

# Solicita a unidade para a qual converter (C, F ou K)
unidade_destino = input("Unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

# Variáveis para armazenar a temperatura convertida
temperatura_convertida = 0

# --- Lógica de Conversão ---

# De Celsius
if unidade_origem == 'C':
    if unidade_destino == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == 'K':
        temperatura_convertida = temperatura + 273.15
    elif unidade_destino == 'C':
        temperatura_convertida = temperatura # Já está na unidade desejada
    else:
        print("Unidade de destino inválida.")

# De Fahrenheit
elif unidade_origem == 'F':
    if unidade_destino == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == 'K':
        temperatura_convertida = ((temperatura - 32) * 5/9) + 273.15
    elif unidade_destino == 'F':
        temperatura_convertida = temperatura # Já está na unidade desejada
    else:
        print("Unidade de destino inválida.")

# De Kelvin
elif unidade_origem == 'K':
    if unidade_destino == 'C':
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == 'F':
        temperatura_convertida = ((temperatura - 273.15) * 9/5) + 32
    elif unidade_destino == 'K':
        temperatura_convertida = temperatura # Já está na unidade desejada
    else:
        print("Unidade de destino inválida.")

# Caso a unidade de origem seja inválida
else:
    print("Unidade de origem inválida.")

# Exibe o resultado da conversão se as unidades forem válidas
if unidade_origem in ['C', 'F', 'K'] and unidade_destino in ['C', 'F', 'K']:
    print(f"\n{temperatura:.2f}{unidade_origem} é igual a {temperatura_convertida:.2f}{unidade_destino}")