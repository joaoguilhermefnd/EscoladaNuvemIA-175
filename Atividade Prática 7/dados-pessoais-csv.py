import csv


def criar_csv_com_dados(nome_arquivo):
    """
    Cria e escreve dados em um arquivo CSV com as colunas 'Nome', 'Idade' e 'Cidade'.

    Args:
        nome_arquivo (str): O nome do arquivo CSV a ser criado.
    """
    # Dados a serem escritos no arquivo
    dados = [
        ['Nome', 'Idade', 'Cidade'],  # Cabeçalho do CSV
        ['Elisabeth Carvalho', 30, 'Fortaleza'],
        ['Thiago Galhardo', 25, 'Camocim'],
        ['Camila Pitanga', 42, 'Pacatuba'],
        ['Roberto Firmino', 35, 'Maranguape']
    ]

    try:
        # Abre o arquivo em modo de escrita ('w') com a codificação UTF-8
        # O 'newline=' evita a criação de linhas em branco extras entre as linhas
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # Cria um objeto 'writer' para escrever no arquivo
            escritor_csv = csv.writer(arquivo_csv)

            # Escreve todas as linhas de uma vez usando 'writerows'
            escritor_csv.writerows(dados)

        print(f"Arquivo '{nome_arquivo}' criado e preenchido com sucesso!")

    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")


# Nome do arquivo que será criado
nome_do_arquivo = 'dados_pessoais.csv'

# Chama a função para criar o arquivo
criar_csv_com_dados(nome_do_arquivo)