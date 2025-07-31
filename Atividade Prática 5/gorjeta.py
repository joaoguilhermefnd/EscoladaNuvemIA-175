def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
  """
  Calcula o valor da gorjeta baseado no valor total da conta e na porcentagem desejada.

  Parâmetros:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

  Retorna:
    float: O valor da gorjeta calculada.
  """
  valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
  return valor_gorjeta

# Solicita o valor da conta ao usuário
try:
  valor_conta = float(input("Digite o valor total da conta: R$ "))
  porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada (ex: 15 para 15%): "))

  gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
  valor_total_com_gorjeta = valor_conta + gorjeta

  print("-" * 30)
  print(f"O valor da conta é: R$ {valor_conta:.2f}")
  print(f"A porcentagem da gorjeta é: {porcentagem_gorjeta}%")
  print(f"O valor da gorjeta a ser deixada é: R$ {gorjeta:.2f}")
  print(f"O valor total a pagar (conta + gorjeta) é: R$ {valor_total_com_gorjeta:.2f}")
  print("-" * 30)

except ValueError:
  print("Entrada inválida. Por favor, digite apenas números.")