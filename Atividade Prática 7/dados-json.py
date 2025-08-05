import json

def escrever_dados_json(nome_arquivo, dados):
    """
    Escreve um dicionário Python em um arquivo JSON.

    Args:
        nome_arquivo (str): O nome do arquivo JSON a ser criado.
        dados (dict): O dicionário com os dados a serem salvos.
    """
    try:
        # Abre o arquivo em modo de escrita ('w')
        # A codificação UTF-8 garante o suporte a caracteres especiais
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            # json.dump() escreve o dicionário no arquivo, formatando-o como JSON
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'!")
    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")

def ler_dados_json(nome_arquivo):
    """
    Lê um arquivo JSON e retorna os dados como um dicionário Python.

    Args:
        nome_arquivo (str): O nome do arquivo JSON a ser lido.

    Returns:
        dict: O dicionário com os dados lidos, ou None em caso de erro.
    """
    try:
        # Abre o arquivo em modo de leitura ('r')
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            # json.load() lê o arquivo e converte o JSON em um dicionário Python
            dados = json.load(arquivo_json)
            return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não é um JSON válido.")
        return None

# --- PARTE 1: ESCREVER OS DADOS NO ARQUIVO ---

# 1. Crie um dicionário com os dados da pessoa
dados_da_pessoa = {
    "nome": "João Fernandes",
    "idade": 30,
    "cidade": "Fortaleza"
}

# 2. Defina o nome do arquivo
nome_do_arquivo = 'dados_pessoa.json'

# 3. Chama a função para escrever os dados
escrever_dados_json(nome_do_arquivo, dados_da_pessoa)

# --- PARTE 2: LER OS DADOS DO ARQUIVO ---

print("\n--- Lendo os dados do arquivo ---")

# 1. Chama a função para ler os dados do arquivo
dados_lidos = ler_dados_json(nome_do_arquivo)

# 2. Exibe os dados lidos, se a leitura foi bem-sucedida
if dados_lidos:
    print(f"Nome: {dados_lidos['nome']}")
    print(f"Idade: {dados_lidos['idade']}")
    print(f"Cidade: {dados_lidos['cidade']}")