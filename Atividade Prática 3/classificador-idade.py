# Solicita a idade do usuário
# Converte a entrada para um número inteiro, pois idade geralmente é um número inteiro
idade = int(input("Digite a sua idade: "))

# Classifica o usuário com base na idade
if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
else:  # Se não se encaixa nas categorias anteriores, deve ser 60 ou mais
    categoria = "Idoso"

# Exibe a categoria do usuário
print(f"Você se encaixa na categoria: {categoria}")