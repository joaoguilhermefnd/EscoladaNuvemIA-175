# Lê o número do funcionário como um inteiro
numero_funcionario = int(input())

# Lê a quantidade de horas trabalhadas como um inteiro
horas_trabalhadas = int(input())

# Lê o valor que o funcionário recebe por hora como um número de ponto flutuante
# É importante usar float() para valores com casas decimais
valor_por_hora = float(input())

# Calcula o salário total multiplicando as horas trabalhadas pelo valor por hora
salario = horas_trabalhadas * valor_por_hora

# Imprime o número do funcionário e o salário formatado
# O f-string permite formatar a saída facilmente:
# {numero_funcionario} insere o valor da variável
# {salario:.2f} formata o salário para duas casas decimais
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = R$ {salario:.2f}")