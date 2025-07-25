# Lê o primeiro nome do vendedor
nome_vendedor = input("Digite o primeiro nome do vendedor: ")

# Lê o salário fixo do vendedor
salario_fixo = float(input("Digite o salário fixo do vendedor (ex: 1500.00): "))

# Lê o total de vendas efetuadas no mês
total_vendas = float(input("Digite o total de vendas efetuadas no mês (ex: 3500.50): "))

# Inicializa a variável de comissão
valor_comissao = 0.0

# --- Lógica para calcular a comissão baseada nas vendas (usando if, elif, else) ---
if total_vendas < 1000.00:
    # Se as vendas forem abaixo de R$ 1.000,00, a comissão é de 5%
    porcentagem_comissao = 0.05
    valor_comissao = total_vendas * porcentagem_comissao
    print(f"Meta de vendas abaixo de R$1.000,00. Comissão de 5%.")
elif total_vendas >= 1000.00 and total_vendas <= 5000.00:
    # Se as vendas forem entre R$ 1.000,00 e R$ 5.000,00, a comissão é de 10%
    porcentagem_comissao = 0.10
    valor_comissao = total_vendas * porcentagem_comissao
    print(f"Meta de vendas entre R$1.000,00 e R$5.000,00. Comissão de 10%.")
else: # total_vendas > 5000.00
    # Se as vendas forem acima de R$ 5.000,00, a comissão é de 15%
    porcentagem_comissao = 0.15
    valor_comissao = total_vendas * porcentagem_comissao
    print(f"Meta de vendas acima de R$5.000,00. Comissão de 15%.")

# Calcula o salário total a receber (salário fixo + valor da comissão)
salario_total = salario_fixo + valor_comissao

# Exibe o total a receber formatado com duas casas decimais
print(f"\nResumo para {nome_vendedor}:")
print(f"Salário Fixo: R$ {salario_fixo:.2f}")
print(f"Total de Vendas: R$ {total_vendas:.2f}")
print(f"Valor da Comissão: R$ {valor_comissao:.2f}")
print(f"TOTAL A RECEBER = R$ {salario_total:.2f}")