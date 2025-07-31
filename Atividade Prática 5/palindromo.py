def eh_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.

    Args:
      texto (str): A string a ser verificada.

    Returns:
      str: "Sim" se for um palíndromo, "Não" caso contrário.
    """
    # Converte para minúsculas e remove espaços e pontuação
    texto_limpo = ''.join(caractere for caractere in texto if caractere.isalnum()).lower()

    # Compara a string limpa com sua versão invertida
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# Solicita a entrada do usuário
entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

# Chama a função e imprime o resultado
resultado = eh_palindromo(entrada)
print(f"A palavra/frase digitada é um palíndromo? {resultado}")