import numpy as np
import re


def analisar_log(caminho_arquivo):
    """
    Lê um arquivo de log, extrai os tempos de execução, e retorna a média
    e o desvio padrão usando a biblioteca numpy.
    """
    try:
        # Abertura do arquivo e leitura de todas as linhas de uma vez
        with open(caminho_arquivo, 'r') as f:
            log_data = f.read()

        # Encontra todos os números que correspondem ao padrão de tempo (ex: 15.23s)
        tempos_str = re.findall(r'(\d+\.?\d*)s', log_data)

        # Converte a lista de strings para um array NumPy de floats
        tempos = np.array([float(t) for t in tempos_str])

        if tempos.size == 0:
            print("Nenhum tempo de execução encontrado no arquivo.")
            return None, None

        # Calcula a média e o desvio padrão de forma direta com numpy
        media = np.mean(tempos)
        desvio_padrao = np.std(tempos)

        return media, desvio_padrao

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None, None


# Nome do seu arquivo de log
nome_do_arquivo = 'log_treinamento.txt'

# Executa a função e exibe os resultados
media_tempo, desvio_padrao_tempo = analisar_log(nome_do_arquivo)

if media_tempo is not None:
    print(f"Média do tempo de execução: {media_tempo:.2f} segundos")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos")