# Define o valor em reais a ser convertido
valor_reais = 100.00

# Define as taxas de câmbio
taxa_dolar = 5.60
taxa_euro = 6.60

# Calcula o valor em dólares
valor_dolar = valor_reais / taxa_dolar

# Calcula o valor em euros
valor_euro = valor_reais / taxa_euro

# Exibe os resultados, arredondados para duas casas decimais
print(f"R$ {valor_reais:.2f} equivalem a:")
print(f"US$ {valor_dolar:.2f}")
print(f"€ {valor_euro:.2f}")