import csv


def ler_e_exibir_csv(nome_arquivo):
    """
    Lê um arquivo CSV, exibe o cabeçalho e depois os dados de cada linha.

    Args:
        nome_arquivo (str): O caminho para o arquivo CSV.
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            # Cria um leitor de CSV que processa o arquivo linha por linha
            leitor_csv = csv.reader(arquivo_csv)

            # Lê a primeira linha, que é o cabeçalho
            cabecalho = next(leitor_csv)
            print(f"Colunas: {', '.join(cabecalho)}\n")

            print("--- Dados das Pessoas ---")
            # Itera sobre cada linha restante e exibe os dados
            for linha in leitor_csv:
                # 'linha' é uma lista, por exemplo: ['Maria Silva', '30', 'São Paulo']
                nome, idade, cidade = linha
                print(f"Nome: {nome:<20} | Idade: {idade:<5} | Cidade: {cidade}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


# Defina o nome do seu arquivo CSV
nome_do_arquivo = 'dados_pessoais.csv'

# Chama a função para executar a leitura e exibição
ler_e_exibir_csv(nome_do_arquivo)