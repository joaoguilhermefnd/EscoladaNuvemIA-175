# Define o nome do produto
nome_produto = "Camiseta"

# Define o preço original do produto
preco_original = 50.00

# Define a porcentagem de desconto
porcentagem_desconto = 20

# Calcula o valor do desconto (preço original * porcentagem / 100)
valor_desconto = preco_original * (porcentagem_desconto / 100)

# Calcula o preço final (preço original - valor do desconto)
preco_final = preco_original - valor_desconto

# Exibe todos os detalhes do produto e do desconto
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")