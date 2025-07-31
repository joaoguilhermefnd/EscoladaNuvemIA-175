import datetime

def calcular_idade_em_dias(ano_nascimento):
  """
  Calcula a idade de uma pessoa em dias, baseada no ano de nascimento.

  Args:
    ano_nascimento (int): O ano de nascimento da pessoa.

  Returns:
    int: A idade em dias.
  """
  hoje = datetime.date.today()
  data_nascimento = datetime.date(ano_nascimento, 1, 1)  # Considera 1º de janeiro do ano de nascimento
  diferenca = hoje - data_nascimento
  return diferenca.days

# Exemplo de uso
try:
  ano = int(input("Digite o ano de nascimento: "))
  idade_dias = calcular_idade_em_dias(ano)
  print(f"Você tem {idade_dias} dias de idade.")
except ValueError:
  print("Entrada inválida. Por favor, digite um ano válido.")