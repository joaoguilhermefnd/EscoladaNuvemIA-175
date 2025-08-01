import random
import string

def gerar_senha(tamanho):
  """
  Gera uma senha aleatória com o tamanho especificado,
  incluindo letras (maiúsculas e minúsculas), números e caracteres especiais.

  Args:
    tamanho: O comprimento desejado para a senha.

  Returns:
    A senha gerada.
  """
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
  return senha

if __name__ == '__main__':
  try:
    tamanho_senha = int(input("Digite a quantidade de caracteres para a senha: "))
    if tamanho_senha <= 0:
      print("O tamanho da senha deve ser um número positivo.")
    else:
      senha_gerada = gerar_senha(tamanho_senha)
      print(f"Sua nova senha é: {senha_gerada}")
  except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")