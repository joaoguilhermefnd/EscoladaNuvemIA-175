import requests


def gerar_perfil_usuario():
    """
    Gera e exibe um perfil de usuário aleatório da API Random User Generator.
    """
    url = 'https://randomuser.me/api/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        dados = response.json()

        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("--- Perfil de Usuário Aleatório ---")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
    except (KeyError, IndexError) as e:
        print(f"Erro ao processar os dados da API: {e}")


if __name__ == '__main__':
    gerar_perfil_usuario()