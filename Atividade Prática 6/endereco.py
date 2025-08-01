import requests

def buscar_endereco_por_cep(cep):
  """
  Busca informações de endereço usando a API ViaCEP a partir de um CEP fornecido.

  Args:
    cep: Uma string contendo o CEP a ser consultado.

  Returns:
    Um dicionário com os dados do endereço se a busca for bem-sucedida,
    ou None em caso de erro.
  """
  url = f"https://viacep.com.br/ws/{cep}/json/"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Lança uma exceção para erros HTTP
    dados = response.json()

    # A API ViaCEP retorna um dicionário com a chave 'erro' se o CEP não for encontrado
    if 'erro' in dados and dados['erro']:
      print("CEP não encontrado.")
      return None
    else:
      return dados

  except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar à API: {e}")
    return None
  except (KeyError, IndexError) as e:
    print(f"Erro ao processar os dados da API: {e}")
    return None

def main():
  """
  Função principal que interage com o usuário e exibe os resultados.
  """
  print("--- Consulta de Endereço por CEP ---")
  cep_digitado = input("Digite o CEP (apenas números): ").strip()

  # Remove qualquer caractere não numérico
  cep_limpo = ''.join(filter(str.isdigit, cep_digitado))

  if len(cep_limpo) != 8:
    print("CEP inválido. Por favor, digite 8 dígitos.")
    return

  endereco = buscar_endereco_por_cep(cep_limpo)

  if endereco:
    print("\n--- Endereço Encontrado ---")
    print(f"CEP: {endereco['cep']}")
    print(f"Logradouro: {endereco['logradouro']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade: {endereco['localidade']}")
    print(f"Estado: {endereco['uf']}")
    print(f"IBGE: {endereco['ibge']}")
  else:
    print("\nNão foi possível obter os dados do endereço.")

if __name__ == "__main__":
  main()