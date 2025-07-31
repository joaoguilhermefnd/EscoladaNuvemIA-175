def calcular_desconto(preco_original, percentual_desconto):
  """
  Calcula o preço final de um produto após a aplicação de um desconto.

  Args:
    preco_original (float): O preço original do produto.
    percentual_desconto (float): O percentual de desconto a ser aplicado.

  Returns:
    float: O preço final do produto com o desconto aplicado.
  """
  valor_desconto = preco_original * (percentual_desconto / 100)
  preco_final = preco_original - valor_desconto
  return preco_final

try:
  preco_produto = float(input("Digite o preço do produto: "))
  percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

  preco_final_produto = calcular_desconto(preco_produto, percentual_desconto)

  print(f"O preço original do produto é: R$ {preco_produto:.2f}")
  print(f"O percentual de desconto é: {percentual_desconto}%")
  print(f"O preço final do produto com desconto é: R$ {preco_final_produto:.2f}")
except ValueError:
  print("Entrada inválida. Por favor, digite apenas números.")