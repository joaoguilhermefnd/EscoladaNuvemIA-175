import requests


def consultar_cotacao(moeda):
    """
    Consulta a cotação de uma moeda estrangeira em relação ao Real Brasileiro (BRL)
    usando a API AwesomeAPI.

    Args:
      moeda: O código da moeda estrangeira (ex: 'USD', 'EUR', 'GBP').

    Returns:
      Um dicionário com os dados da cotação se a busca for bem-sucedida,
      ou None em caso de erro.
    """
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP

        dados = response.json()

        # A API retorna a cotação dentro de uma chave dinâmica, como 'USDBRL'
        chave_cotacao = f"{moeda}BRL"
        if chave_cotacao in dados:
            return dados[chave_cotacao]
        else:
            print(f"Moeda '{moeda}' não encontrada ou código inválido.")
            return None

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
    print("--- Consulta de Cotação de Moedas ---")
    print("Moedas disponíveis: USD (Dólar), EUR (Euro), GBP (Libra Esterlina), JPY (Iene), etc.")

    moeda_desejada = input("Digite o código da moeda desejada (ex: USD): ").strip().upper()

    cotacao = consultar_cotacao(moeda_desejada)

    if cotacao:
        data_timestamp = int(cotacao['timestamp'])
        from datetime import datetime
        data_atualizacao = datetime.fromtimestamp(data_timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print("\n--- Informações da Cotação ---")
        print(f"Moeda: {cotacao['name']}")
        print(f"Valor Atual (Compra): R$ {float(cotacao['bid']):.2f}")
        print(f"Valor Máximo (Alta): R$ {float(cotacao['high']):.2f}")
        print(f"Valor Mínimo (Baixa): R$ {float(cotacao['low']):.2f}")
        print(f"Última Atualização: {data_atualizacao}")
    else:
        print("\nNão foi possível obter os dados da cotação.")


if __name__ == "__main__":
    main()