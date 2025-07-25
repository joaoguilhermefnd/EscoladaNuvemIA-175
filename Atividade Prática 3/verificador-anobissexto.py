# Solicita ao usuário que digite um ano
ano = int(input("Digite um ano: "))

# Variável para armazenar o resultado da verificação
e_bissexto = False

# Verifica se o ano é bissexto
# Um ano é bissexto se for divisível por 4 E (não for divisível por 100 OU for divisível por 400)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    e_bissexto = True
else:
    e_bissexto = False

# Exibe o resultado
if e_bissexto:
    print(f"O ano {ano} É bissexto.")
else:
    print(f"O ano {ano} NÃO é bissexto.")